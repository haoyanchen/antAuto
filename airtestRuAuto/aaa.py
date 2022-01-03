from airtest.core.api import *
from airtest.cli.parser import cli_setup
import os
from PIL import Image
import pytesseract



#
# if not cli_setup():
#     auto_setup(__file__, logdir='./reuse/log')
#
#
# def dianji():
#     print("aaaaaaaaaa")
#     print(os.getcwd())
#     touch(Template(os.getcwd()+"\\reuse\\img\\tpl1637587933540.png", record_pos=(0.102, 0.192), resolution=(2280, 1080)))

# print(os.getcwd())
image = Image.open(os.getcwd()+"\\reuse\\img\\tpl1637521250730.png")
image1 = Image.open(os.getcwd()+"\\reuse\\img\\tpl1637488379134.png")
text = pytesseract.image_to_string(image, lang='chi_sim', config="--psm 6")
text1 = pytesseract.image_to_string(image1, lang='chi_sim', config="--psm 6")
print("结果如下：")
print(text)
print(text1)