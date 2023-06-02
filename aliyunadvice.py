import cv2

if __name__ == '__main__':
    video = "http://admin:admin@192.168.3.58:8081/"

    capture = cv2.VideoCapture(video)
    print("success,连接成功")
    face_cascade = cv2.CascadeClassifier('D:\python code\opencv\opencvmodel\haarcascade_frontalface_default.xml')#改成绝对路径
    num = 0

    while True:
        success, image = capture.read()

        key = cv2.waitKey(10)
        if key == 27:
            print("esc 关闭...")
            break


        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image_gray, 1.3, 4)

        for x, y, width, height in faces:
            cv2.rectangle(image, (x, y), (x + width, y + height), color=(0, 0, 255), thickness=2)
        cv2.imshow("image", image)