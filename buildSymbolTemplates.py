import glob
import os

import cv2
from buildStateTemplates import states

PATH = "templates/symbol_templates-1/"

class Image():
    def __init__(self, image):
        self.image = image
        self.location = 0

def extractDesignFeatures(img):
    '''
    Extract the features of a plate to get a standard
    template for a state's license plate design
    '''
    # extract design features from license plate
    sift = cv2.SIFT_create(nOctaveLayers=4, sigma=1.6)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(gray, None)

    # return state templates
    return (kp, des)


def createAllSymbolTemplates():
    """
    Create all the state design templates
    """
    symbol_templates = {}
    for state in states:
        search = PATH + state.lower().replace(' ','') + '.*jpg'
        symbol_list = glob.glob(PATH + state.lower().replace(' ', '') + '*.jpg')
        if (len(symbol_list)):
            symbol_templates[state] = {}
            for symbol in symbol_list:
                symbol_image = cv2.imread(symbol)
                symbol_template = extractDesignFeatures(symbol_image)
                symbol_templates[state][symbol] = symbol_template

    # return all state design tempates
    return symbol_templates
