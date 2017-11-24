# -*- coding: utf-8 -*-

import os

import cv2
#F:\tangka_minyuansaomiao
input_data = 'F:/tangka_minyuansaomiao/'
output_data = 'F:/tangka_minyuansaomiao_change/'

def get_files():
    size=(208,208)
    for file in os.listdir(input_data):
        file_path = input_data+file
        img = cv2.imread(file_path)
        try:
            imgc = cv2.resize(img,size,interpolation=cv2.INTER_AREA)
            cv2.imwrite(output_data + file,imgc)
            print (file)
        except:
            print ('exception')
            pass
        
       