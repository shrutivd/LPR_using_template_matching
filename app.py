import cv2
import sys
import buildStateTemplates as st
import licensePlateRecognition as pr
import extractDriverInformation as di

def main(lp_img):
    # build state templates
    state_temp = pr.buildTemplates()
    img = cv2.imread(sys.argv[1])
    # get state
    state = pr.findState(img, state_temp)
    # get letters/numbers
    # get driver's information
    name = di.getDriverName(state, 'INNS')

    # print license plate information
    print('---------------------------------------')
    print('State:', state)
    print('License Plate:', 'INNS')
    print("Driver's Name:", name)
    print('---------------------------------------')


if __name__ == "__main__":
    main(sys.argv)
