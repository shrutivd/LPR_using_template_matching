import cv2
import numpy as np
import buildStateTemplates as st


def buildTemplates():
    state_templates = st.createAllStateTemplates()
    # create number and letter templates
    # letter_number_templates = 

    return state_templates# , letter_number_templates


def findState(img, state_templates):
    img_features = st.extractDesignFeatures(img)

    bf = cv2.BFMatcher()

    match_size = 0
    state = ''
    matches_list = []
    loop_broken = 0
    for curr_state in st.states:
        curr_template = state_templates[curr_state]
        matches = bf.knnMatch(curr_template[1], img_features[1],k=2)
        verified_matches = []
        for match1, match2 in matches:
            if match1.distance < 0.7 * match2.distance:
                verified_matches.append([match1])
        match_size = len(verified_matches)
        state = curr_state
        matches_list.append(match_size)
        if match_size > 60:
            loop_broken = 1
            break

    if loop_broken == 0:
        match_size = max(matches_list)
        state = st.states[matches_list.index(match_size)]

    return state
