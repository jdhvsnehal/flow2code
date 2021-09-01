from io import StringIO
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import pandas as pd
import time
import os
import sys
import pytesseract

DATAPATH = './test/'

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\tanvi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

st.title('Flowchart--2--Code')
st.header('FLOWCHART')
page = st.selectbox("", ["Upload Your Image", "Select Flowchart"])

if page == "Upload Your Image":
 st.header("Upload image")
 file_path = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
 
 if file_path is not None:
  image = Image.open(file_path)
  st.image(image)
  cong = r'-l eng --oem 3 --psm 6'

  text = pytesseract.image_to_string(image, config=cong)
  f = open('output.txt', 'w')
  f.write(text)
  f.close()

  file = open('code.txt', 'w')
  sys.stdout = file

  f = open('output.txt')
  for line in f:
     line = line.lower()
     line = line.strip('\n')
     if "start" in line:
       print("#include<stdio.h>\nvoid main()\n{")
     if "input" in line:
       print(line.replace("input", "int"), ";")
       print(line.replace("input", "scanf:"), ";")
     if "=" in line:
       print(line, ";")
     if "if" in line:
       print(line)
     if "true" in line:
       print(line.replace("true","\t")
         .replace("false","\nelse\n\t")
         .replace("print", "printf:"))
     elif "print" in line:
       print(line.replace("print", "printf:"), ";")
     if "stop" in line:
       print(line.replace("stop","}"))
  f.close()
  file.close()

  f1 = open('code.txt', 'r')
  content = f1.read()
  f1.close()

if page == "Select Flowchart":
 st.header("Select flowchart")

 sample = st.selectbox("",["Hello","Sum of two numbers","Average of two numbers","Simple Interest","Maximum of two numbers"])
     
 if sample == "Hello":
      image = cv2.imread(DATAPATH + "Hello.png")
 if sample == "Sum of two numbers":
      image = cv2.imread(DATAPATH + "Sum of two numbers.png")
 if sample == "Average of two numbers":
      image = cv2.imread(DATAPATH + "Average of two numbers.png")
 if sample == "Simple Interest":
      image = cv2.imread(DATAPATH + "Simple Interest.png")
 if sample == "Maximum of two numbers":
      image = cv2.imread(DATAPATH + "Maximum of two numbers.png")

 st.image(DATAPATH + sample + ".png")

 cong = r'-l eng --oem 3 --psm 6'

 text = pytesseract.image_to_string(image, config=cong)

 f = open('output.txt', 'w')
 f.write(text)
 f.close()

 file = open('code.txt', 'w')
 sys.stdout = file

 f = open('output.txt')
 for line in f:
     line = line.lower()
     line = line.strip('\n')
     if "start" in line:
       print("#include<stdio.h>\nvoid main()\n{")
     if "input" in line:
       print(line.replace("input", "int"), ";")
       print(line.replace("input", "scanf:"), ";")
     if "=" in line:
       print(line, ";")
     if "if" in line:
       print(line)
     if "true" in line:
       print(line.replace("true","\t")
         .replace("false","\nelse\n\t")
         .replace("print", "printf:"))
     elif "print" in line:
       print(line.replace("print", "printf:"), ";")
     if "stop" in line:
       print(line.replace("stop","}"))
 f.close()
 file.close()

 f1 = open('code.txt', 'r')
 content = f1.read()
 f1.close()

convert = st.button('Convert')
 
if convert:     
      st.header('CODE')  
      code = content
      st.code(code, language='c')

