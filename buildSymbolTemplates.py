import cv2
import random

symbols = ['A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y',
               'Z', '0', '1', '2', '3', '4', 
               '5', '6', '7', '8', '9']


def extractDesignFeatures(img):
    '''
    Extract the features of a plate to get a standard
    template for a state's license plate design
    '''
    # extract design features from license plate
    sift = cv2.SIFT_create()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(gray, None)

    # return state templates
    return (kp, des)


def createAllSymbolTemplates():
    """
    Create all the state design templates
    """
    symbol_templates = {}
    for symbol in symbols:
        symbol_image = cv2.imread('templates/symbol_templates/' + symbol + '.jpg')
        symbol_template = extractDesignFeatures(symbol_image)
        symbol_templates[symbol] = symbol_template

    # return all state design tempates
    return symbol_templates
