import string
import sys
import random
from PIL import Image,ImageDraw,ImageFont

'''生成随机验证码'''

def Capture(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

'''验证码生成图片'''
def Capture_img():
    # 定义使用Image类实例化一个长为120px,宽为30px,基于RGB的(255,255,255)颜色的图片
    img1 = Image.new(mode="RGB", size=(120, 30), color=(255, 255, 255))
    # 实例化一支画笔
    draw1 = ImageDraw.Draw(img1, mode="RGB")
    # 定义要使用的字体
    font1 = ImageFont.truetype('arial.ttf', 36)
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw1.text([24,0], Capture(), color1, font=font1)
    # 把生成的图片保存为"pic.png"格式
    pngPath=sys.path[1]+"\\static\pic.png"
    print(pngPath)
    with open(pngPath, "wb") as f:
        img1.save(f, format="png")

Capture_img()

