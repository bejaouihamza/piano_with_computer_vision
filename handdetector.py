import cv2
import mediapipe as mp
import time
import numpy as np

class HandDetector:
    def __init__(self,mode=False,maxHands=1,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,min_detection_confidence=self.detectionCon,min_tracking_confidence=self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img



    def findPosition(self,img,handNo=0,draw=True):   #default parameters
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                h,w,_=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(0,255,0),cv2.FILLED)
                    if id==4:
                        cv2.circle(img,(cx,cy),5,(0,0,0),cv2.FILLED)
                    elif id==5:
                        cv2.putText(img,'re',(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),3)
                    elif id==8:
                        cv2.putText(img,'mi',(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),3)
                    elif id==12:
                        cv2.putText(img,'fa',(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),3)
                    elif id==16:
                        cv2.putText(img,'sol',(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),3)
                    elif id==20:
                        cv2.putText(img,'la',(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),3)
                    elif id==17:
                        cv2.putText(img,'si',(cx,cy),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),3)
            
            # Calculate and draw the 'do' position it's not like the others
            if len(lmList) >= 6:  
                do_x = (lmList[2][1] + lmList[5][1]) // 2
                do_y = (lmList[2][2] + lmList[5][2]) // 2
                cv2.line(img,(lmList[2][1],lmList[2][2]),(lmList[5][1],lmList[5][2]),(255,255,255),2) #add line
                cv2.circle(img, (do_x, do_y), 5, (0, 255, 0), cv2.FILLED)   #add circle
                cv2.putText(img, 'do', (do_x, do_y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 255), 3)
                lmList.append([21, do_x, do_y])     # Add 'do' position to the lmList list

        return lmList



def distance(lmList,epsilon):
    if len(lmList)<22:  
        return [False]*7

    thumb=np.array(lmList[4][1:])  # Thumb as reference point
    
                          # Calculate distances 
    landmarks = [21,5,8,12,16,20,17]          # Use 21 for 'do'
    notes=[np.linalg.norm(np.array(lmList[i][1:])-thumb)<=epsilon for i in landmarks]
    
    return notes

def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    detector=HandDetector()

    while True:

        success,img=cap.read()
        if not success:
            break

        img=cv2.flip(img,1)
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            notes_on=distance(lmList,30)  
            print(notes_on)

        cTime=time.time()
        fps=1/(cTime-pTime) #calculate fps
        pTime=cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255),3)
        cv2.imshow("Image",img)

        if cv2.waitKey(1) and 0xFF==ord('q'): #break if 'q' is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()