import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # 读取影片得用法  原理就是读取图片快速形成视频
penColorBGT = [[81, 52, 100, 111, 245, 22], [46, 150, 45, 80, 32, 231], [10, 200, 150, 31, 253, 253]]
drawpoint = []
penColorHSV = [[0, 0, 0], [255, 255, 255], [135, 135, 135]]


def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow('hav',hav)
    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])
        mask = cv2.inRange(hsv, lower, upper)
        # cv2.imshow('mask', mask)
        result = cv2.bitwise_and(img, img, mask=mask)
        penx, peny = findContour(mask)
        # cv2.imshow('result', result)
        cv2.circle(imgContour, (penx, peny), 10, penColorBGT[i], cv2.FILLED)
        if peny != -1:
            drawpoint.append([penx, peny, i])


def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)

    return x + w // 2, y


def draw(drawpoints):
    for i in drawpoints:
        cv2.circle(imgContour, (i[0], i[1]), 10, penColorBGT[i[2]], cv2.FILLED)


if __name__ == '__main__':
    while True:
        ret, frame = cap.read()  # ret表示是否读取成功
        if ret:
            imgContour = frame.copy()
            cv2.imshow('video', frame)
            findPen(frame)
            draw(drawpoint)
            cv2.imshow('contour', imgContour)
        else:
            break

        if cv2.waitKey(1) == ord('q'):  # 影片得播放速度,ord(q)按键条件
            break
