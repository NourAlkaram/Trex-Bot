from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
import os


def createCard(number , ratio , color):
    (W , H) = (25*ratio , 35*ratio)
    img = Image.new("RGBA", size=(W, H) , color=color)
    img = ImageOps.expand(img,border=3,fill="White")
    edit = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('NATS.ttf', 20*ratio)
    w, h = edit.textsize(str(number) , font=myFont)
    edit.text(((W-w)/2,(H-h)/2),font=myFont ,text=str(number), fill="White")
    return img
    

image1 = createCard(1 , 3 , "blue")
image2 = createCard(2 , 3 , "green")
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
#new_image.save("merged_image.jpg","JPEG")
new_image.show()
#os.remove(path='merged_image.jpg')
