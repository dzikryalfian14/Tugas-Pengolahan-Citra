import cv2

vangog = cv2.imread("gog_ai.png", 0)

image = cv2.flip(vangog, 0) #flip vertikal dengan parameter 0
image2 = cv2.flip(vangog, 1) #flip horizontal dengan parameter 1
cv2.imshow("original", vangog)
cv2.imshow("Flip Vertikal", image)
cv2.imshow("Flip Horizontal", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
