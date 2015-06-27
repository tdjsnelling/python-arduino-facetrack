import cv2, sys, serial

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(1)
scr_width = int(video_capture.get(3))
scr_height = int(video_capture.get(4))

ser = serial.Serial(
    port='/dev/ttyACM3', # teensy port
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.open()

i = 0

while True:
	# capture frames
	ret, frame = video_capture.read()
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		grey,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	# draw rectangle around the faces, and detect face position
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (128, 128, 128), 2)

		if x+(w/2) > (scr_width/2) + 20: # if centre of face is on right of screen
			cv2.line(frame, ((scr_width/2) + 20, 0), ((scr_width/2) + 20, scr_height), (0, 0, 255), 1)
			if i % 8 == 0: # poll every 8 frames
				ser.write('2') # send data to teensy
		elif x+(w/2) < (scr_width/2) - 20: # if centre of face is on left of screen
			cv2.line(frame, ((scr_width/2) - 20, 0), ((scr_width/2) - 20, scr_height), (0, 0, 255), 1)
			if i % 8 == 0:
				ser.write('1')


	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	i += 1

# release all
ser.close()
video_capture.release()
cv2.destroyAllWindows()




