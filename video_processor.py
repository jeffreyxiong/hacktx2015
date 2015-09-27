# game_screen.py
# Hack TX 2015 - Eddie Dugan, Jeffrey Xiong, May Zhong, Xilin Liu

import cv2
import numpy
from matplotlib import pyplot as plt


class video_processor:
    # processes videos for characters,
    # stages, games, and results

    def __init__(self, video_file):
        # assert type string
        assert isinstance(video_file, str)
        # initialize vars
        self.filename = video_file
        self.CHARACTERS = []
        self.STAGES = []
        self.GAMESCREEN = 'game.png'

    def process(self):
        cap = cv2.VideoCapture(self.filename)

        chars = []
        stages = []
        games = 0
        results = []

        check_stage = True
        check_char = False
        check_game = False
        check_result = False
        ret, frame = cap.read()
        frame = frame[1:2, 2:3]

        while cap.isOpened():
            ret, frame = cap.read()
            # first, match go!
            # if go! is a match, check character, set go to false

            if check_stage:
                stage_var = self.__match_stage(frame)
                if stage_var[0]:
                    stages.append((games + 1, stage_var[1]))
                    check_stage = False
                    check_char = True

            if check_char:
                char_var = self.__match_characters(frame)
                if char_var[0]:
                    chars.append((games + 1, char_var[1]))
                    check_char = False
                    check_game = True

            if check_game:
                if self.__match_game(frame):
                    games += 1
                    check_game = False
                    check_result = True

            if check_result:
                result_var = self.__match_result(frame)
                if result_var[0]:
                    results.append((games, result_var[1]))
                    check_result = False
                    check_stage = True

        cap.release()

        return chars, stages, games, results

    def __match_characters(self, frame):
        screencap = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        for character in self.CHARACTERS:
            print(character)
        return

    def __match_stage(self, frame):
        stages = []
        accuracy = 0
        return accuracy, stages

    def __match_game(self, frame):
        # determines whether a screencap shows the end of a game

        # initialize images
        img = frame
        img2 = img.copy()

        template = cv2.imread(self.GAMESCREEN, 0)
        w, h = template.shape[::-1]

        methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED']
        matches = []
        # template-matching
        for meth in methods:
            img = img2.copy()
            method = eval(meth)
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            print(meth + '------')
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc

            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img, top_left, bottom_right, 255, 2)

            if max_val > 0.9:
                print(max_val)
                plt.subplot(121), plt.imshow(res, cmap='gray')
                plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                plt.subplot(122), plt.imshow(img, cmap='gray')
                plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                plt.suptitle(method)
                plt.show()
                matches.append(max_val)
        if len(matches) == 2:
            return True
        else:
            return False

    def __match_result(self, frame):
        return






