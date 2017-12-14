import pytesseract
from PIL import Image
path='C:/Users/hao.k.wang/Desktop/python opencv/oldproject/My-Python/img/t5.jpg'
#tessdata_dir_config='--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
image = Image.open(path)
image.load()  # 加载一下图片，防止报错，此处可省略
image.show()  # 调用show来展示图片，调试用，可省略
code = pytesseract.image_to_string(image, lang='chi_sim')
#code = pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)
#code = pytesseract.image_to_string(image)

print(code)