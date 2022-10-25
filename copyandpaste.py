import cv2

vangog = cv2.imread("gog_ai.png", 0)
h,w = vangog.shape[:2]
resize_img = cv2.resize(vangog, (w//3, h//3))
heigh, width = resize_img.shape[:2]


pipheigh = 0 #koordinat y
pipwidth = 0 #koordinat x
vangog[pipheigh:pipheigh+heigh,pipwidth:pipwidth+width] = resize_img

cv2.imwrite(r'.\dump_pip.png',vangog)
cv2.imshow("Cut and paste",vangog)
cv2.waitKey(0)
cv2.destroyAllWindows()