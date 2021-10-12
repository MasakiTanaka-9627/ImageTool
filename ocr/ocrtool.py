from PIL import Image as OCR_Image
import sys
import pyocr
import pytesseract

def function():    
    tools = pyocr.get_available_tools()
    tool = tools[0]
    txt = tool.image_to_string(
        OCR_Image.open('media/images/test.png'),
        lang="jpn",
    )
    return txt
