import multiprocessing as mp
from CntBlinkAddFile import *
from GUI_main import *

def gui():
    #print("/\/\/\/\/\/\/\/\/\/waiting for data uploaded.../\/\/\/\/\/\/\/\/")
    #evt.wait()
    print("/\/\/\/\/\/\/\/\/\/starting GUI/\/\/\/\/\/\/\/\/\/")
    app = QtWidgets.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    image_viewer1 = ImageViewer()
    vid.VideoSignal1.connect(image_viewer1.setImage)
    push_button1 = QtWidgets.QPushButton('Start Video')
    push_button2 = QtWidgets.QPushButton('Stop Video')
    push_button1.clicked.connect(vid.startVideo)
    push_button2.clicked.connect(vid.stopVideo)
    vertical_layout = QtWidgets.QVBoxLayout()
    horizontal_layout = QtWidgets.QHBoxLayout()    
    vertical_layout.addLayout(horizontal_layout)
    vertical_layout.addWidget(push_button1)
    vertical_layout.addWidget(push_button2)
    horizontal_layout.addWidget(image_viewer1)
    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)
    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())

def cntBlinkAddFile():
  print("starting cntBlinkAddFile------------------------------------------------------------")
  IMG_SIZE = (34, 26)
  cnt_blink = 0
  cnt_list = []
  exit_condition = True

  detector = dlib.get_frontal_face_detector()
  # 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\shape_predictor_68_face_landmarks.dat'
  # 'resource/data/shape_predictor_68_face_landmarks.dat'
  predictor = dlib.shape_predictor('resource/data/shape_predictor_68_face_landmarks.dat')
  # 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\models\\2018_12_17_22_58_35.h5'
  # 'resource/models/2018_12_17_22_58_35.h5'
  model = load_model('resource/models/2018_12_17_22_58_35.h5')
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
        eye_img_l, eye_rect_l = crop_eye(IMG_SIZE, gray, gray, eye_points=shapes[36:42])
        eye_img_r, eye_rect_r = crop_eye(IMG_SIZE, gray, gray, eye_points=shapes[42:48])
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
      #fin_elem = (cnt_blink, int(duration))
      #cnt_list.append(fin_elem)
      cnt_list.append(cnt_blink)    
    
    print("10 sec past")
    #print(cnt_list)
    #C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\dataset\\count_blink.csv
    #
    file_name = 'resource/data/count_blink.csv'
    with open(file_name, 'w', newline='') as f:
      writer = csv.writer(f)
      writer.writerows([cnt_list])
    
    #evt.set()

    #여기서부터 GUI
    #cnt_list 데이터를 그래프로 나타내기
    #만약 gui 파일 이름이 GUI, 메소드 이름이 drawGraph라면
    #위에 import GUI
    #GUI.drawGraph(cnt_list)

    #마지막에 필요(강제종료인 경우)
    if(exit_condition == False):
      break


if __name__ == '__main__':
    t1 = mp.Process(target=cntBlinkAddFile, args=())
    t2 = mp.Process(target=gui, args=())
    t1.start()
    t2.start()