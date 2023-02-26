import cv2
import numpy as np
import buildLetterTemplates as lt


def buildTemplates():
    character_templates = lt.createAllCharactersTemplates()

    return character_templates


def findCharacter(img, character_templates):
    img_features = lt.extractDesignFeatures(img)

    bf = cv2.BFMatcher()

    match_size = 0
    character = []
    matches_list = []
    for curr_character in lt.characters:
        curr_template = character_templates[curr_character]
        matches = bf.knnMatch(curr_template[1], img_features[1],k=2)
        verified_matches = []
        for match1, match2 in matches:
            if match1.distance < 0.7 * match2.distance:
                verified_matches.append([match1])
        match_size = len(verified_matches)
        matches_list.append(match_size)
        temp = cv2.drawMatchesKnn(character_templates['img' + curr_character],curr_template[0],img,img_features[0],verified_matches,None)
        cv2.imshow("test",temp)
        cv2.waitKey(0)
        print(match_size)
        if match_size > 20:
            character.append(curr_character)

    return character