import cv2
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


def individualSymbols(image):
    # crop image
    cropped_image = crop_image(image)

    # convert image to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    gray_image[gray_image > 100], gray_image[gray_image <= 100] = 255, 0

    #blur image
    gray_image = cv2.medianBlur(gray_image,1)
    gray_image = cv2.medianBlur(gray_image, 5)

    # convert image to binary
    binaryImage = gray_image.clip(0,1)
    binaryImage = binaryImage - 1

    # convert image to binary
    color_binary_image = np.zeros((gray_image.shape[0],gray_image.shape[1],3),dtype=np.uint8)
    color_binary_image[gray_image==255] = 255

    # create contours
    thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    
    # get bounding boxes from contour
    filenames = []
    for i in range(len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        cv2.rectangle(cropped_image, (x, y), (x + w, y + h), (255,0,0), 4)

        # check to make sure the rectangle is big enough
        # to contain a symbol
        if h >= 100 and w >= 100:
            croppedImg = cropped_image[y:y + h, x:x + w]
            filename = "cropped_images_templates/template" + str(i) + ".jpg"
            filenames.append(filename)
            cv2.imwrite(filename, croppedImg)

    return filenames
