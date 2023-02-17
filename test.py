import cv2
import buildStateTemplates as st
import licensePlateRecognition as pr

num_tests = [3, 3, 3, 6, 23, 4, 29, 14, 5, 4,
    3, 13, 3, 2, 1, 1, 4, 3, 5, 3, 14,
    4, 12, 1, 5, 4, 2, 20, 13, 5, 3,
    4, 4, 3, 1, 1, 4, 9, 4, 2,
    1, 9, 2, 2, 7, 2, 4, 23, 3, 3]

if __name__ == "__main__":
    state_temp = pr.buildTemplates()
    for state in st.states:
        print("--------------------", state)
        for i in range(num_tests[st.states.index(state)]):
            img = cv2.imread('testImages/' + state.lower().replace(' ', '') + '/' + str(i + 1) + '.jpg')
            print(pr.findState(img, state_temp))
