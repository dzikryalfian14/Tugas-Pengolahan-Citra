import cv2
img = cv2.imread('sudoku.png')

p = 1.25
new_width = int(img.shape[1] * p)
new_height = int(img.shape[0] * p)
resized = cv2.resize(img, (new_width, new_height))

cv2.imshow(f"Elephants at scale {p}", resized)
# Hide the image window with any key press
cv2.waitKey()
cv2.destroyAllWindows()
