#!/usr/bin/env python3
import sys
import os
import face_recognition

image_1_encoding = []
image_2_encodings = []
count = 0
path_1 = '/home/aikansh/Images/'
path_2 = '/home/aikansh/'
def recognizer(a,b):
   image_1 = face_recognition.load_image_file(path_2 + a)
   image_1_encoding = face_recognition.face_encodings(image_1)
   image_2 = face_recognition.load_image_file(path_1 + b)
   image_2_encodings = face_recognition.face_encodings(image_2)
   count = 0
   for image_2_encoding in image_2_encodings:
       matches = face_recognition.compare_faces(image_1_encoding, image_2_encoding)
       if True in matches:
          count = 1
   if count == 1:
      return 1
   else:
      return 0

