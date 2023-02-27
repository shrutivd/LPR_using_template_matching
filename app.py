import cv2
import sys
import buildStateTemplates as st
import buildSymbolTemplates as syt
import licensePlateRecognition as pr
import extractDriverInformation as di
import imageToData as td

def main(lp_img):
    # build state templates
    state_temp, symbol_temp = pr.buildTemplates()
    img = cv2.imread(sys.argv[1])
    # get state
    state = pr.findState(img, state_temp)
    # get letters/numbers
    cropped_symbols = td.individualSymbols(img)
    symbols = pr.findSymbols(cropped_symbols, symbol_temp)
    # get driver's information
    name = di.getDriverName(state, symbols)

    # print license plate information
    print('---------------------------------------')
    print('State:', state)
    print('License Plate:', symbols)
    print("Driver's Name:", name)
    print('---------------------------------------')


if __name__ == "__main__":
    main(sys.argv)
