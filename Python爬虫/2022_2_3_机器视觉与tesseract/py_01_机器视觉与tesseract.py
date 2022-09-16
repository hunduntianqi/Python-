"""
    OCR:
        光学字符识别(Optical Character Recognition), 通过扫描等光学输入方式将各种票据, 报刊, 书籍, 文稿
    及其他印刷品的文字转换为图像信息, 再利用文字识别技术将图像信息转化为电子文本
    tesseract-ocr:
        OCR的一个底层识别库, 由Google维护的开源OCR识别库
    pytesseract:
        Python模块, 是对tesseract-ocr做的一层API封装
        使用示例:
            import pytesseract
            from PIL import Image # python图片处理库
            img = Image.open('test1.jpg') # 创建图片字符串
            result = pytesseract.image_to_string(img) # 图片转字符串
            print(result)

"""
# tesseract-ocr Python接口模块
import pytesseract
# python的图片处理库
from PIL import Image

# 创建图片对象
img = Image.open('./img/a.jpg')
# 图片转字符串
result = pytesseract.image_to_string(img)
print(result)