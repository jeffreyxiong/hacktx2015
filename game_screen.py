# game_screen.py
# Hack TX 2015 - Eddie Dugan, Jeffrey Xiong, May Zhong, Xilin Liu

import cv2
import video_parser
import numpy
from matplotlib import pyplot as plt

# capture end-game screen


def test_methods(screencaps, template_file):
    for img in screencaps:
        print(img)
        match_game_screen(img, template_file)


def match_game_screen(screencap, template_file):
    # determines whether a screencap shows the end of a game

    # initialize images
    img = cv2.imread(screencap, 0)
    img2 = img.copy()

    template = cv2.imread(template_file, 0)
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED']
    matches = {}
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

    return matches


test_methods(['game_sc1.png', 'game_sc2.png', 'game_sc3.png', 'game_sc4.png', 'game_sc5.png', 'game_sc6.png', 'game_sc7.png'],
             'game.png')
