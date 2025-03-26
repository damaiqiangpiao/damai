import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        print(
            result.multi_hand_landmarks
        )
        imgHeight = img.shape[0]
        imgWight = img.shape[1]
        if result.multi_hand_landmarks:
            for handlms in result:
                mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
                for i, lm in enumerate(handlms.landmark):
                    xpos = int(lm.x * imgWight)
                    ypos = int(lm.y * imgHeight)
                    # cv2.putText(img,str(i),(xpos-25,ypos+5),cv2.FONT_HERSHEY_SIMPLEX,)
        cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break
