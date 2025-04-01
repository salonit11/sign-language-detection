import os
import pickle
import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt

mp_hands= mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'
data=[]
labels=[]
for dir_ in os.listdir(DATA_DIR):
    dir_path= os.path.join(DATA_DIR,dir_)
    if not os.path.isdir(dir_path):
        continue

    for imgpath in os.listdir(os.path.join(DATA_DIR,dir_)):
        data_aux = []
        x_=[]
        y_=[]
        img = cv2.imread(os.path.join(DATA_DIR, dir_, imgpath))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks: # extracting landmarks for all images
                # mp_drawings.draw_landmarks(
                #     img_rgb, # input
                #     hand_landmarks, # output
                #     mp_hands.HAND_CONNECTIONS,
                #     mp_drawing_styles.get_default_hand_landmarks_style(),
                #     mp_drawing_styles.get_default_hand_connections_style())
#         plt.figure()
#         plt.imshow(img_rgb)
# plt.show()
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_)) # creating array of all landmarks

            if len(data_aux)==42:
                data.append(data_aux) # array representing all image's landmarks
                labels.append(dir_) # name of directory of each image

f = open('data.pickle','wb')
pickle.dump({'data':data,'labels':labels},f)
f.close()
