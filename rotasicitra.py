import cv2

rotasi = int(input("derajat rotasi: "))
warna = int(input("Warna grayscale(0) or berwarna(1): "))
vangog = cv2.imread("gog_ai.png", warna)
cv2.imshow("original", vangog)

h, w = vangog.shape[:2]
center = (w//2, h//2)

image = cv2.getRotationMatrix2D(center, rotasi, 1) # (center, rotasi, skala)

putar = cv2.warpAffine(vangog, image, (w, h)) #
cv2.imshow(f"Rotated by {rotasi} Degrees", putar)
cv2.waitKey(0)
cv2.destroyAllWindows()
