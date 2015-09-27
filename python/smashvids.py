import cv2

METHODS = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF_NORMED']
METHOD = 'cv2.TM_SQDIFF_NORMED'

CHARACTERS = ["stocks/" + x for x in ["bowser.png", "cptfalcon.png", "dk.png", "drmario.png", "falco.png", "fox.png",
                                      "gamewatch.png", "ganon.png", "iceclimber.png", "jigglypuff.png", "kirby.png",
                                      "link.png", "luigi.png", "mario.png", "marth.png", "mewtwo.png", "ness.png",
                                      "peach.png", "pichu.png", "pikachu.png", "roy.png", "samus.png", "sheik.png",
                                      "yoshi.png", "younglink.png", "zelda.png"]]

def get_combatants(filepath):
    assert isinstance(filepath, str) # needs to be a string - filepath

    # load (and gray out?) the image
    screencap = cv2.cvtColor(cv2.imread(filepath).copy(), cv2.COLOR_BGR2GRAY)

    potentials = {}
    for character in CHARACTERS:
        template = cv2.cvtColor(cv2.imread(character).copy(), cv2.COLOR_BGR2GRAY)
        locs = []
        for meth in METHODS:
            method = eval(meth)
            w, h = template.shape[::-1] # returns 3 for colored, 2 when grayed out
            result = cv2.matchTemplate(screencap, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if method == cv2.TM_SQDIFF_NORMED:
                top_left = min_loc
                quality = 1 - min_val
            else:
                top_left = max_loc
                quality = max_val
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # tuple of tuples ((TLX, TLY), (BRX, BRY)) zero is top/left of image
            locs.append(((top_left, bottom_right), quality))
        # # do they agree?
        for i in range(2):
            for j in range(2):
                if i != j:
                    if locs_equal(locs[i][0], locs[j][0]):
                        potentials[character] = (locs[i][0], locs[i][1] + locs[j][1]) # sum quality

    if (len(potentials) == 0):
        return []

    # now check for vertical equality
    agreement_sets = [] #lists of character names
    for char in potentials:
        if len(agreement_sets) == 0:
            agreement_sets.append([char])
        else:
            for set in agreement_sets:
                if locs_y_in_range(potentials[set[0]][0], potentials[char][0]):
                    set.append(char)
                else:
                    agreement_sets.append([char])

    combatants = max(agreement_sets, key = lambda l : sum([potentials[x][1] for x in l]))
    return [x[7:] for x in combatants]

def locs_equal(loc1, loc2):
    return loc1[0][0] == loc2[0][0] and loc1[0][1] == loc2[0][1] and loc1[1][0] == loc2[1][0] and loc1[1][1] == loc2[1][1]

def locs_y_in_range(loc1, loc2):
    return abs(loc1[0][1] - loc2[0][1]) < 4