import cv2
import numpy as np
from buildSymbolTemplates import Image

cropping_characteristics = {
    "New Hampshire": (1.7, 2.4),
    "California": (2.4, 1.5),
    "Nevada": (2.4, 1.5),
    "Utah": (2.4, 1.5),
    "Washington": (2.4, 1.5),
    "West Virginia": (2.4, 1.5),
    "_": (2.0, 1.8)
}
def crop_image(img, state):
    if state in cropping_characteristics.keys():
        top, bottom = cropping_characteristics[state]
    else:
        top, bottom = cropping_characteristics["_"]

    height_scale_measure = 0.53
    center_y = img.shape[0] / 2
    height_scaled = img.shape[0] * height_scale_measure
    top_y, bottom_y = center_y - height_scaled / top, center_y + height_scaled / bottom
    img_cropped = img[int(top_y):int(bottom_y), :]
    return img_cropped


def individualSymbols(image, state):

    # crop the complere image of number plate to focus just
    # on area where characters are present
    cropped_image = crop_image(image, state)

    # convert image to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur to remove the noise from the image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 25)

    # showImage(edges)

    # create contours
    thresh_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    dark_letter_image = cv2.bitwise_not(thresh_image)
    contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_height = cropped_image.shape[0]

    # get bounding boxes from contour
    croppedLetters = []
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        padding = 10
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(dark_letter_image.shape[1] - x, w + padding * 2)
        h = min(dark_letter_image.shape[0] - y, h + padding * 2)

        # check to make sure the rectangle is big enough
        # to contain a symbol
        if h >= max_height * 0.75 and w >= max_height * 0.25:
            croppedImg = Image(np.zeros((h, w, 3), dtype=np.uint8))
            croppedImg.image[:, :, 0] = dark_letter_image[y:y + h, x:x + w ]
            croppedImg.image[:, :, 1] = dark_letter_image[y:y + h, x:x + w ]
            croppedImg.image[:, :, 2] = dark_letter_image[y:y + h, x:x + w ]

            croppedImg.location = x

            croppedLetters.append(croppedImg)

    return croppedLetters