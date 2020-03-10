#this script written for the cv final code q1, creating a picture with font'HELLO WORLD'
#coded by TJX 09/07/2019

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#create the new picture with size 130x35, color=white
new_image=Image.new('RGB',(130,35),'white')
#set the text
text='HELLO WORLD'
#use the ImageFont to set the font properties
font_text=ImageFont.truetype("C:\Windows\Fonts\Bahnschrift.ttf",size=15)
#create the object
thing=ImageDraw.Draw(new_image)
#set the ink color
thing.ink=0+0*256+0*256*256
#the position of the text is [10,10]
thing.text([10,10],text,font=font_text)
#save the image
new_image.save(r'C:\Users\tangj\Desktop\hello_world.jpeg')