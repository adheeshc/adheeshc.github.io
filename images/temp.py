# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-03-22 16:15:16
# Last Modified time: 2020-03-22 16:22:02

import cv2

frame=cv2.imread("bg_1.jpeg")

scale_percent=10

width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

frame=cv2.resize(frame,dsize)
cv2.imwrite('bg_2.jpeg',frame)
cv2.imshow("frame",frame)

cv2.waitKey(0)
cv2.destroyAllWindows()