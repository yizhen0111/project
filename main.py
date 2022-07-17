import cv2
import numpy

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
    gray = cv2.medianBlur(gray, 5)



    rows = gray.shape[0]
    circles = cv2.HoughCircles(
        gray,  # 灰度
        cv2.HOUGH_GRADIENT,  # OpenCV
        1,  # 分辨率的反比
        rows / 8,  # 行
        param1=100,  # 內部邊緣監測的上限值
        param2=30,  # 中心檢測值
        minRadius=20,  # 最小半徑 的判斷
        maxRadius=50  # 最大半徑 的判斷
    )

    # 繪製的圓形如果存在(成功繪製)
    if circles is not None:
        circles = numpy.uint16(numpy.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])

            x = center[0]
            y = center[1]

            # circle center 圓心
            cv2.circle(frame,
                      center,  # 圓心位置
                      1,  # 繪製圓形的半徑
                      (0, 0, 255),  # 線條顏色
                      3  # 線條寬度
                      )

            # circle outline
            radius = i[2]
            cv2.circle(frame,
                      center,  # 圓心位置
                      radius,  # 半徑長度
                      (0, 0, 0),  # 線條顏色
                      2  # 線條寬度
                      )

            z = radius / 2
            z = int(z)
            print(z)

            # 右塞

            r = x + z
            cv2.circle(frame,
                      (r, y),  # 圓心位置
                      1,  # 繪製圓形的半徑
                      (0, 100, 100),  # 線條顏色
                      3  # 線條寬度
                      )
            print(1)

            # 左塞
            l = x - z
            cv2.circle(frame,
                      (l, y),  # 圓心位置
                      1,  # 繪製圓形的半徑
                      (0, 100, 100),  # 線條顏色
                      3  # 線條寬度
                      )

            # 上塞
            u = y + z
            cv2.circle(frame,
                      (x, u),  # 圓心位置
                      1,  # 繪製圓形的半徑
                      (0, 100, 100),  # 線條顏色
                      3  # 線條寬度
                      )

            # 下塞
            d = y - z
            cv2.circle(frame,
                      (x, d),  # 圓心位置
                      1,  # 繪製圓形的半徑
                      (0, 100, 100),  # 線條顏色
                      3  # 線條寬度
                      )



    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()