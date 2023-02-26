import cv2
import numpy as np
import buildStateTemplates as st


def buildTemplates():
    state_templates = st.createAllStateTemplates()
    # create number and letter templates
    # letter_number_templates = 

    return state_templates# , letter_number_templates


def findMatches(img, state_templates):
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


def findState(img, state_templates):
    img_features = st.extractDesignFeatures(img)
    match_size = 0
    state = ''
    matches_list = []
    loop_broken = 0
    
    for i in range(len(state_templates)):
        keypoint_matches = {}
        curr_template = state_templates[st.states[i]]
        for j in range(len(curr_template[1])):
            dists = []
            dist_dict = {}
            matches = []
            for k in range(len(img_features[1])):
                dist = np.linalg.norm(curr_template[1][j] - img_features[1][k])
                dists.append(dist)
                dist_dict[dist] = [img_features[0][k].pt[0], img_features[0][k].pt[1], dist]

            # add two shortest distances to matches
            matches.append(dist_dict[min(dists)])
            dists.remove(min(dists))
            matches.append(dist_dict[min(dists)])
            keypoint_matches[curr_template[0][j]] = matches

        # ratio test
        list_pairs_matched_keypoints = []
        for point in curr_template[0]:
            p2 = keypoint_matches[point][0]
            p3 = keypoint_matches[point][1]
            if p2[2] < p3[2] * 0.7:
                list_pairs_matched_keypoints.append(
                    [[point.pt[0], point.pt[1]], [p2[0], p2[1]]])


        match_size = len(list_pairs_matched_keypoints)
        state = st.states[i]
        matches_list.append(match_size)
        if match_size > 60:
            loop_broken = 1
            break

    if loop_broken == 0:
        match_size = max(matches_list)
        state = st.states[matches_list.index(match_size)]

    return state
