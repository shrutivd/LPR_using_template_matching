import cv2

if __name__ == "__main__":
    img = cv2.imread("cropped_images_templates/template48.jpg")
    sift = cv2.SIFT_create()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(gray, None)

    img = cv2.drawKeypoints(gray,kp,img)
    cv2.imwrite('HI.jpg',img)