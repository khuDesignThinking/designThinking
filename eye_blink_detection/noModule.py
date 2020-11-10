import cv2, dlib
import numpy as np
from imutils import face_utils
from keras.models import load_model
import time

def crop_eye(img, eye_points):
  x1, y1 = np.amin(eye_points, axis=0)
  x2, y2 = np.amax(eye_points, axis=0)
  cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
  w = (x2 - x1) * 1.2
  h = w * IMG_SIZE[1] / IMG_SIZE[0]
  margin_x, margin_y = w / 2, h / 2
  min_x, min_y = int(cx - margin_x), int(cy - margin_y)
  max_x, max_y = int(cx + margin_x), int(cy + margin_y)
  eye_rect = np.rint([min_x, min_y, max_x, max_y]).astype(np.int)
  eye_img = gray[eye_rect[1]:eye_rect[3], eye_rect[0]:eye_rect[2]]
  return eye_img, eye_rect

IMG_SIZE = (34, 26)
cnt_blink = 0
cnt_list = []
exit_condition = True

detector = dlib.get_frontal_face_detector()
# 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\shape_predictor_68_face_landmarks.dat'
# 'resource/data/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor('C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\shape_predictor_68_face_landmarks.dat')
# 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\models\\2018_12_17_22_58_35.h5'
# 'resource/models/2018_12_17_22_58_35.h5'
model = load_model('C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\models\\2018_12_17_22_58_35.h5')
model.summary()

cap = cv2.VideoCapture(0)

# if(종료 버튼 누르면):  <== GUI로 구현   현재는 그런 기능 안넣음 강제종료 못함
#     exit_condition = False

#실행 종료 버튼 누르기 전까지 계속 실행
while (True):
  #10초 동안 눈 감은 횟수 판단
  duration = -1 #강제 실행 종료인지 판단하는 인덱스
  start_time = time.time()
  eye_condition = "initialize"
  while (True):
    if not cap.isOpened():
      print("video open error")
      exit(100)
    ret, img_ori = cap.read()  
    if not ret :
      print("img read error")
      exit(100)
    img_ori = cv2.resize(img_ori, dsize=(0, 0), fx=0.5, fy=0.5)
    img = img_ori.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:  
      shapes = predictor(gray, face)
      shapes = face_utils.shape_to_np(shapes)
      eye_img_l, eye_rect_l = crop_eye(gray, eye_points=shapes[36:42])
      eye_img_r, eye_rect_r = crop_eye(gray, eye_points=shapes[42:48])
      eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
      eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
      eye_img_r = cv2.flip(eye_img_r, flipCode=1)
      eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
      eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
      pred_l = model.predict(eye_input_l)
      pred_r = model.predict(eye_input_r)
      if(pred_l <= 0.1 and pred_r <= 0.1 and eye_condition == "non-blinked"):
        eye_condition = "blinked"
        cnt_blink += 1
        print("blinked")
      elif(pred_l <= 0.1 and pred_r <= 0.1 and eye_condition == "blinked"):
        print("deleted...")
        #None
      else:
        eye_condition = "non-blinked"    
    
    curr_time = time.time()
    if( (curr_time - start_time) > 10 ):
      break
    elif(exit_condition == False):
      duration = curr_time - start_time
      break 

  if(duration == -1 or int(duration) == 0):
    cnt_list.append(cnt_blink)
    cnt_blink = 0
    start_time = time.time()
  else:
    fin_elem = (cnt_blink, int(duration))
    cnt_list.append(fin_elem)    
  
  print("10 sec past")
  print(cnt_list)
  
  #여기서부터 GUI
  #cnt_list 데이터를 그래프로 나타내기
  #만약 gui 파일 이름이 GUI, 메소드 이름이 drawGraph라면
  #위에 import GUI
  #GUI.drawGraph(cnt_list)
  
  #마지막에 필요(강제종료인 경우)
  if(exit_condition == False):
    break
