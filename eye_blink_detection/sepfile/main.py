import detectBlink as blink
from keras.models import load_model
import dlib
import time
# 10초마다 cnt 리턴
detector = dlib.get_frontal_face_detector()
# 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\shape_predictor_68_face_landmarks.dat'
# 'resource/data/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor('C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\shape_predictor_68_face_landmarks.dat')
# 'C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\models\\2018_12_17_22_58_35.h5'
# 'resource/models/2018_12_17_22_58_35.h5'
model = load_model('C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\models\\2018_12_17_22_58_35.h5')
model.summary()
IMG_SIZE = (34, 26)
prev_eye_condition = "non-blinked"
cnt_blink = 0
cnt_list = []

exit_condition = True
# if(종료 버튼 누르면):  <== GUI로 구현   현재는 그런 기능 안넣음 강제종료 못함
#     exit_condition = False
while(True):
    #10초 동안 계속 사진찍고 판단
    duration = -1 #강제 실행 종료인지 판단하는 인덱스
    start_time = time.time()
    while(True):
        eye_condition = blink.defCondition(IMG_SIZE, detector, predictor, model)
        # 성능이 안좋아서 필요 없을 듯
        #if(eye_condition == "blinked" and prev_eye_condition == "non-blinked"):
        if(eye_condition == "blinked"):
            #prev_eye_condition = "blinked"
            print("blinked")
            cnt_blink += 1
        # 성능이 안좋아서 필요 없을 듯
        # elif(eye_condition == "blinked" and prev_eye_condition == "blinked"):
        #     print("deleted...")
        else:
            #prev_eye_condition = "non-blinked"
            print("non-blinked")
        
        curr_time = time.time()
        if(curr_time - start_time > 10):
            break
        elif(exit_condition == False):
            duration = curr_time - start_time
            break
    
    # print("10 sec past")
    # print(cnt_blink)
    
    if(duration == -1 or int(duration) == 0):
        cnt_list.append(cnt_blink)
    else:
        fin_elem = (cnt_blink, int(duration))
        cnt_list.append(fin_elem)
    
    print(cnt_list)
    #여기서부터 GUI     위에 import 필요
    #cnt_list 데이터를 그래프로 나타내기
    #만약 gui 메소드 이름이 drawGraph라면 
    #drawGraph(cnt_list)
    
    #마지막에 필요(강제종료인 경우)
    if(exit_condition == False):
       break
