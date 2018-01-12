import cv2 as cv
import numpy as np
import time;
from matplotlib import pyplot as plt
import pyautogui, sys
img_rgb = cv.imread('jazz_cap.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('jazz_obj.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    pyautogui.moveTo(pt[0] + (w / 2), pt[1] + (h / 2))
    pyautogui.click()

ts = time.time()
cv.imwrite('res_' + str(ts) + '.png',img_rgb)