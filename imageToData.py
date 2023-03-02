import datetime

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # your path may be different
import cv2
import os
import numpy as np

def crop_image(img):
    width_scale_measure = 0.95
    height_scale_measure = 0.53
    center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
    width_scaled, height_scaled = img.shape[1] * width_scale_measure, img.shape[0] * height_scale_measure
    left_x, right_x = center_x - width_scaled / 2, center_x + width_scaled / 2
    top_y, bottom_y = center_y - height_scaled / 2, center_y + height_scaled / 2
    img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
    return img_cropped


image_list = os.listdir('./reserve')
print(image_list)

plate = 1
for image in image_list:
    read_image = cv2.imread('./reserve/'+image)
    cropped_image = crop_image(read_image)
    # convert to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    gray_image[gray_image > 100], gray_image[gray_image <= 100] = 255, 0

    gray_image = cv2.medianBlur(gray_image,1)
    gray_image = cv2.medianBlur(gray_image, 5)


    binaryImage = gray_image.clip(0,1)
    binaryImage = binaryImage - 1
    print(binaryImage)
    contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    contours_poly = [None] * len(contours)
    # The Bounding Rectangles will be stored here:
    boundRect = []

    # Alright, just look for the outer bounding boxes:
    for i, c in enumerate(contours):
        if hierarchy[0][i][3] == -1:
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            boundRect.append(cv2.boundingRect(contours_poly[i]))

    color_binary_image = np.zeros((gray_image.shape[0],gray_image.shape[1],3),dtype=np.uint8)
    color_binary_image[gray_image==255] = 255

    cv2.imshow('image', color_binary_image)
    cv2.waitKey(0)


    # Draw the bounding boxes on the (copied) input image:
   # for i in range(len(boundRect)):
   #     color = (0, 255, 0)
   #     cv2.rectangle(color_binary_image, (int((boundRect[i][0])), int((boundRect[i][1]))), \
   #         (int((boundRect[i][0] + boundRect[i][3])), int((boundRect[i][1] + boundRect[i][3]))), color, 2)

    # Crop the characters:
    for i in range(len(boundRect)):
        # Get the roi for each bounding rectangle:
        x, y, w, h = boundRect[i]
        # Crop the roi:
        croppedImg = color_binary_image[y:y + h + 10, x:x + w + 10]
        filename = "./cropped_images_template/template{0}_{1}.jpg"
        cv2.imwrite(filename.format(plate,i), croppedImg)
        plate = plate + 1
       # cv2.waitKey(0)