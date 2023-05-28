import cv2


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier('D:\python code\opencv\opencvmodel\haarcascade_frontalface_default.xml')#文件路径（）绝对路径

while True:

    _, image = cap.read()

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
    faces = face_cascade.detectMultiScale(image_gray, 1.1, 2)

    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    cv2.imshow("image", image)
    key = cv2.waitKey(10)
    if key == 27:
        print("esc break...")
        break

cap.release()
cv2.destroyAllWindows()
