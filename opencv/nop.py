import pytesseract
from PIL import Image
path='C:/Users/hao.k.wang/Desktop/python opencv/oldproject/My-Python/img/t6.jpg'
#tessdata_dir_config='--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
image = Image.open(path)
image.load()  # 加载一下图片，防止报错，此处可省略
image.show()  # 调用show来展示图片，调试用，可省略
code = pytesseract.image_to_string(image) #, lang='chi_sim'
#code = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
#code = pytesseract.image_to_string(image)
print(image.size)
print(code)
tuple_part_img_corp = (0,0,1024,200)
new_image=image.crop(tuple_part_img_corp)
new_image.load()
new_image.show()
new_code=pytesseract.image_to_string(new_image)
print(new_code)