import cv2, dlib
import numpy as np
from imutils import face_utils

def defCondition(IMG_SIZE, detector, predictor, model):
  """사진 하나 찍고 눈 깜빡임 판별"""
  #사진 한 장 찍음
  cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
  ret, img_ori = cap.read()
  if not ret :
    print("failed")
    return "failed"
  #얼굴 및 눈 인식
  img_ori = cv2.resize(img_ori, dsize=(0, 0), fx=0.5, fy=0.5)
  img = img_ori.copy()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = detector(gray) 
  eye_condition = ""
  for face in faces:  
    shapes = predictor(gray, face)
    shapes = face_utils.shape_to_np(shapes)

    eye_img_l, eye_rect_l = crop_eye(IMG_SIZE, gray, eye_points=shapes[36:42])
    eye_img_r, eye_rect_r = crop_eye(IMG_SIZE, gray, eye_points=shapes[42:48])

    eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
    eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
    eye_img_r = cv2.flip(eye_img_r, flipCode=1)

    eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
    eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.

    pred_l = model.predict(eye_input_l)
    pred_r = model.predict(eye_input_r)

    #눈 깜빡임 판별
    # state_l = 'O' if pred_l > 0.1 else '-'
    # state_r = 'O' if pred_r > 0.1 else '-'
    if(pred_l <= 0.1 and pred_r <= 0.1):
      #print("blinked")
      eye_condition =  "blinked"
    else:
      #print("non-blinked")
      eye_condition = "non-blinked"
  return eye_condition 

def crop_eye(IMG_SIZE, gray, eye_points):
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