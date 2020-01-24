import tesserocr
from PIL import Image

image = Image.open("4.png")
# 灰度化
image = image.convert("L")
# 二值化，传入的是数字 1，默认阈值是 127。一般不推荐使用，因为不够灵活
# image = image.convert("1")

# 另一种二值化。自定义灰度，将灰度值在 115 以上的设置 1（白色），其它设为 0（黑色），相当于将阈值设置成了 115
table = [1] * 256
for i in range(256):
    table[i] = 0
    if i > 150:
        break

image = image.point(table, "1")

print(tesserocr.image_to_text(image))