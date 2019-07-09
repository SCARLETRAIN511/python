from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
new_image=Image.new('RGB',(130,35),'white')

text='HELLO WORLD'
font_text=ImageFont.truetype("C:\Windows\Fonts\Bahnschrift.ttf",size=15)
thing=ImageDraw.Draw(new_image)
thing.ink=0+0*256+0*256*256
thing.text([10,10],text,font=font_text)
new_image.save(r'C:\Users\tangj\Desktop\hello_world.jpeg')