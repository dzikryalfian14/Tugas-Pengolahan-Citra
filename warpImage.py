import cv2
import numpy as np

array = np.zeros((4,2), int)
counter = 0
def click(event,x,y,flags,param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(vangog,(x,y),5,(255,0,0),-1)
        array[counter] = x, y
        counter = counter + 1
        #print(x,y)

vangog = cv2.imread('sudoku.png')
vangog = cv2.resize(vangog, (700,500))

while True:
    if counter == 4:
        pts1 = np.float32([[array[0], array[1],array[2],array[3]]])
        pts2 = np.float32([[[0,0], [500,0],[0,500],[500,500]]])
        matriks = cv2.getPerspectiveTransform(pts1, pts2)
        final = cv2.warpPerspective(vangog, matriks, (500,500))
        cv2.imshow("Wrap Image", final)

    cv2.namedWindow('Original')
    cv2.setMouseCallback('Original', click)

    cv2.imshow('Original', vangog)
    cv2.waitKey(1)

cv2.destroyAllWindows()
