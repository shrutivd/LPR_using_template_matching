import cv2
import buildStateTemplates as st
import licensePlateRecognition as pr
import extractDriverInformation as di

num_tests = [3, 6, 3, 6, 23, 4, 29, 14, 5, 4,
    3, 13, 3, 2, 1, 1, 4, 3, 5, 3, 14,
    4, 12, 1, 4, 4, 2, 20, 13, 5, 3,
    4, 4, 3, 1, 1, 4, 9, 4, 2,
    1, 9, 2, 2, 7, 2, 4, 23, 3, 3]

if __name__ == "__main__":
    # test state recognition
    state_temp = pr.buildTemplates()
    for state in st.states:
        print("--------------------", state)
        for i in range(num_tests[st.states.index(state)]):
            img = cv2.imread('testImages/' + state.lower().replace(' ', '') + '/' + str(i + 1) + '.jpg')
            print(pr.findState(img, state_temp))

    # test finding driver's name
    print(di.getDriverName('Maine', 'INNS')) # Sarah Summers
    print(di.getDriverName('Utah', 'B059JK')) # Brian Dunlap
    print(di.getDriverName('California', '6UCP708')) # Lisa Morrow
    print(di.getDriverName('South Dakota', '1BLV44')) # Chad Miller
