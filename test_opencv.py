import cv2
import numpy as np

img = cv2.imread('1.png')

cv2.circle(img,(500,500),200,(255,0,0),thickness=5)
# template = cv2.imread('s.png')
# w, h = template.shape[:-1]

# res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
# threshold = .8
# loc = np.where(res >= threshold)
# for pt in zip(*loc[::-1]):  # Switch columns and rows
    # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('2.png', img)
print(img.shape)