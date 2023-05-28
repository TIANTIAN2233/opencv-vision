import cv2

#创建新的cam对象
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#初始化人脸识别器（默认的人脸haar级联）
face_cascade = cv2.CascadeClassifier('D://python code//opencv//haarcascade_frontalface_default.xml')

while True:
    # 从摄像头读取图像
    _, image = cap.read()
    # 转换为灰度
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 检测图像中的所有人脸
    faces = face_cascade.detectMultiScale(image_gray, 1.1, 2)
    # 为每个人脸绘制一个蓝色矩形
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    cv2.imshow("image", image)
    key = cv2.waitKey(10)
    if key == 27:
        print("esc break...")
        break

cap.release()
cv2.destroyAllWindows()
