import cv2

# read image and write image.

# second flag is for how image should be read  3 flags : 1 is color image, 0 is grayscale mode, -1 is same as it is.\
img = cv2.imread('lena.jpg', -1)

# it will give you the matrix
print (img)

# this will show the image for a millisecod. We could use the waitKey to let it show for longer.
cv2.imshow('image', img)
# put 0 as a parameter. It would let it wait until the close key
key = cv2.waitKey(5000)

if(key == 27):
# this method would destroy every window you opened
    cv2.destroyAllWindows()
elif key == ord('s'):
    # write the image to another file. Could save as any type of file.
    cv2.imwrite('lena_copy.png', img)