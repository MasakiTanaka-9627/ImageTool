from PIL import Image as OCR_Image
import sys
import pyocr
import pytesseract

def function():
    TESSERACT_PATH = './.apt/usr/share/tesseract-ocr'
    TESSDATA_PATH = './.apt/usr/share/tesseract-ocr/4.00/tessdata'

    
    tools = pyocr.get_available_tools()
    tool = tools[0]
    txt = tool.image_to_string(
        OCR_Image.open('media/images/test.png'),
        lang="jpn",
    )
    return txt
