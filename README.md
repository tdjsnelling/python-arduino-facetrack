# python / arduino face tracking

This is a project I started with the aim of getting a motorised camera to follow my face.

I have used Haar Cascades and OpenCV for the face tracking, and a teensy 2.0 to control the stepper motor. 

If the face is in the left of the frame, a specific integer is sent to the teensy and the motor is controlled accordingly - likewise if the face is in the right of the frame. 

A quick demo:
![rec](recorded.gif)
