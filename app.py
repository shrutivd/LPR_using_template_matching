import cv2
import sys
import argparse
import licensePlateRecognition as pr
import extractDriverInformation as di
import imageToData as td

def mainFrontend(lp_img, fast=False):
    # build state templates
    state_temp, symbol_temp = pr.buildTemplates()
    img = cv2.imread(lp_img)
    # get state
    if fast:
        state = pr.findStateFast(img, state_temp)
    else:
        state = pr.findState(img, state_temp)
    # get letters/numbers
    cropped_symbols = td.individualSymbols(img, state)
    if fast:
        symbols = pr.findSymbolsFast(state, cropped_symbols, symbol_temp)
    else:
        symbols = pr.findSymbols(state, cropped_symbols, symbol_temp)
    # get driver's information
    try:
        name, email, phone, bday = di.getDriverName(state, symbols)

        # print license plate information
        print('---------------------------------------')
        print("Driver's Name:", name)
        print("Driver's Date of Birth:", bday)
        print('State:', state)
        print('License Plate:', symbols)
        print("Driver's Email:", email)
        print("Driver's Phone Number:", phone)
        print('---------------------------------------')

        return [name, state, symbols, email, phone, bday]
    except:
        # print license plate information
        print('---------------------------------------')
        print('Match not found')
        print('State:', state)
        print('License Plate:', symbols)
        print('---------------------------------------')

        return [state, symbols]

def main(lp_img):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fast", help="Faster matching", action='store_true', required=False)
    parser.add_argument('img', type=str, help='License plate image file location')
    args = parser.parse_args()
    # build state templates
    state_temp, symbol_temp = pr.buildTemplates()
    img = cv2.imread(args.img)
    # get state
    if args.fast:
        state = pr.findStateFast(img, state_temp)
    else:
        state = pr.findState(img, state_temp)
    # get letters/numbers
    cropped_symbols = td.individualSymbols(img, state)
    if args.fast:
        symbols = pr.findSymbolsFast(state, cropped_symbols, symbol_temp)
    else:
        symbols = pr.findSymbols(state, cropped_symbols, symbol_temp)
    # get driver's information
    name, email, phone, bday = di.getDriverName(state, symbols)

    # print license plate information
    print('---------------------------------------')
    print("Driver's Name:", name)
    print("Driver's Date of Birth:", bday)
    print('State:', state)
    print('License Plate:', symbols)
    print("Driver's Email:", email)
    print("Driver's Phone Number:", phone)
    print('---------------------------------------')

    return name, state, symbols, email, phone, bday


if __name__ == "__main__":
    main(sys.argv)
