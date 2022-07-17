import cv2
import numpy as np

cap = cv2.VideoCapture('test.mp4')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉換成灰階

    rows = gray.shape[0]
    circles = cv2.HoughCircles(
        gray,  # 灰度
        cv2.HOUGH_GRADIENT,  # OpenCV
        1,  # 分辨率的反比
        rows / 8,  # 行
        param1=100,  # 內部邊緣監測的上限值
        param2=30,  # 中心檢測值
        minRadius=1,  # 最小半徑 的判斷
        maxRadius=100  # 最大半徑 的判斷
    )

    # 繪製的圓形如果存在(成功繪製)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])

            x = center[0]
            y = center[1]
            print(x)
            print(y)

            # circle center 圓心
            cv2.circle(gray,
                      center,  # 圓心位置
                      1,  # 繪製圓形的半徑
                      (0, 100, 100),  # 線條顏色
                      3  # 線條寬度
                      )

            # circle outline
            radius = i[2]
            cv.circle(gray,
                      center,  # 圓心位置
                      radius,  # 半徑長度
                      (255, 0, 255),  # 線條顏色
                      3  # 線條寬度
                      )

    # gray = cv2.cvtColor(frame, 6)  # 也可以用數字對照 6 表示轉換成灰階
    cv2.imshow('oxxostudio', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()