import cv2

if __name__ == '__main__':

    cv2.namedWindow("camera", 1)

    video = "http://admin:admin@192.168.3.58:8081/"  
    capture = cv2.VideoCapture(video)

    num = 0
    while True:
        success, img = capture.read()
        cv2.imshow("camera", img)
        key = cv2.waitKey(10)
        if key == 27:
            # esc键断开连接
            print("esc break...")
            break
