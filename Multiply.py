import cv2

I = cv2.imread('gog_ai.png', 0)
J = cv2.multiply(I, 3)


cv2.imshow("Gambar 1", I)
cv2.imshow("Multiply", J)
cv2.waitKey(60000)
cv2.destroyAllWindows()