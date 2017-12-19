#coding=utf8

import pytesseract
import re
from PIL import Image


a= '解释器用相应的encoding去解释python代码'
print a

path='C:/Users/hao.k.wang/Desktop/tesseract_train/jpg/心.jpg'
tessdata_dir_config='--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
image = Image.open(path)
image.load()  # 加载一下图片，防止报错，此处可省略
image.show()  # 调用show来展示图片，调试用，可省略
#code = pytesseract.image_to_string(image) #, lang='chi_sim'
code = pytesseract.image_to_string(image, lang='osd', config=tessdata_dir_config)
#code = pytesseract.image_to_string(image, lang='chi_sim')
print(image.size)
print(code)
tuple_part_img_corp = (908,0,1816,160)
new_image=image.crop(tuple_part_img_corp)
new_image.load()
new_image.show()
new_code=pytesseract.image_to_string(new_image, lang='chi_sim', config=tessdata_dir_config)
print(new_code)