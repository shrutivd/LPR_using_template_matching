import cv2
import numpy as np
from buildSymbolTemplates import Image


def crop_image(img):
    height_scale_measure = 0.53
    center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
    height_scaled = img.shape[0] * height_scale_measure
    top_y, bottom_y = center_y - height_scaled / 2, center_y + height_scaled / 2
    img_cropped = img[int(top_y):int(bottom_y), :]
    return img_cropped

def showImage(img):
    cv2.imshow("img",img)
    cv2.waitKey(0)
def individualSymbols(image):

    # crop image
    cropped_image = crop_image(image)

    # convert image to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # blur image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 25)
    showImage(blurred_image)

    # showImage(edges)

    # create contours
    thresh_image = cv2.threshold(blurred_image, 110, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_height = cropped_image.shape[0]

    showImage(thresh_image)
    # get bounding boxes from contour
    filenames = {}
    for i in range(len(contours)):
        x,y,w,h = cv2.boundingRect(contours[i])
        padding = 15
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(thresh_image.shape[1] - x, w + padding * 2)
        h = min(thresh_image.shape[0] - y, h + padding * 2)

        # cv2.rectangle(gray_image, (x, y), (x + w, y + h), (255,0,0), 4)


        # check to make sure the rectangle is big enough
        # to contain a symbol
        if h >= max_height * 0.75 and w >= max_height * 0.25:
            croppedImg = Image(np.zeros((h,w,3),dtype=np.uint8))
            croppedImg.image[:, :, 0] = thresh_image[y:y + h, x:x + w ]
            croppedImg.image[:, :, 1] = thresh_image[y:y + h, x:x + w ]
            croppedImg.image[:, :, 2] = thresh_image[y:y + h, x:x + w ]

            filenames[croppedImg] = x
            showImage(croppedImg.image)

    return filenames
