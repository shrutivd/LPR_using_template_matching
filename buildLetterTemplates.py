import cv2
import os


characters  = os.listdir("cropped_images_template")

def extractDesignFeatures(img):
    '''
    Extract the features of a plate to get a standard
    template for a state's license plate design
    '''
    # extract design features from license plate
    sift = cv2.SIFT_create()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(img, None)

    # return state templates
    return (kp, des)


def createAllCharactersTemplates():
    """
    Create all the state design templates
    """
    character_templates = {}
    for character in characters:
           #input image from test images
        character_image = cv2.imread('./cropped_images_template/' + character)

        character_template = extractDesignFeatures(character_image)
        character_templates[character] = character_template
        character_templates['img' + character] = character_image

    # return all character design templates
    return character_templates
