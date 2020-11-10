import cv2, dlib
import numpy as np
from imutils import face_utils
from keras.models import load_model
import time
import variable as v

IMG_SIZE = (34, 26)

detector = dlib.get_frontal_face_detector()
# 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\shape_predictor_68_face_landmarks.dat'
# 'resource/data/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\models\\2018_12_17_22_58_35.h5'
# 'resource/models/2018_12_17_22_58_35.h5'
model = load_model('models/2018_12_17_22_58_35.h5')
model.summary()

def crop_eye(gray, img, eye_points):
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


def blink_detect():
  cap = cv2.VideoCapture(0)
  v.cnt_blink = 0
  eye_condition = "initialize"

  v.start_time = time.time()
  cnt_list = []

  while cap.isOpened():
    ret, img_ori = cap.read()
  
    if not ret :
      break

    img_ori = cv2.resize(img_ori, dsize=(0, 0), fx=0.5, fy=0.5)

    img = img_ori.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    faces = detector(gray)
  
    for face in faces:  
      shapes = predictor(gray, face)
      shapes = face_utils.shape_to_np(shapes)

      eye_img_l, eye_rect_l = crop_eye(gray,img, eye_points=shapes[36:42])
      eye_img_r, eye_rect_r = crop_eye(gray,img, eye_points=shapes[42:48])

      eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
      eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
      eye_img_r = cv2.flip(eye_img_r, flipCode=1)

      eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
      eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.

      pred_l = model.predict(eye_input_l)
      pred_r = model.predict(eye_input_r)

      # visualize
      state_l = 'O' if pred_l > 0.1 else '-'
      state_r = 'O' if pred_r > 0.1 else '-'

      if(pred_l <= 0.1 and pred_r <= 0.1 and eye_condition == "non-blinked"):
        eye_condition = "blinked"
        v.cnt_blink += 1
        print("blinked")
      elif(pred_l <= 0.1 and pred_r <= 0.1 and eye_condition == "blinked"):
        print("deleted...")
      else:
        eye_condition = "non-blinked"
    
      state_l = state_l % pred_l
      state_r = state_r % pred_r
      Text = "Blinks : " + str(v.cnt_blink)

      cv2.rectangle(img, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(255,255,255), thickness=2)
      cv2.rectangle(img, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255,255,255), thickness=2)
    
      cv2.putText(img, state_l, tuple(eye_rect_l[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
      cv2.putText(img, state_r, tuple(eye_rect_r[0:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)   
      cv2.putText(img, Text, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    cv2.imshow('result', img)
  
    v.curr_time = time.time()
    if( (v.curr_time - v.start_time) > 10 ):
      print("10 sec past")
      cnt_list.append(v.cnt_blink)
      v.cnt_blink = 0
      v.start_time = time.time()
  
    if cv2.waitKey(1) == ord('q'):
      v.end_time = time.time()
      duration = v.end_time - v.start_time
      if(int(duration) >= 1):
        cnt_list.append( (v.cnt_blink, int(duration)) )
      print("BlinkCount per 10 sec list")
      print(cnt_list)
      break