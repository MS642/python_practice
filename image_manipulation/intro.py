from PIL import Image
mac = Image.open('example.jpg')
#mac.show()
mac.size
mac.format_description

# start coordinate then the end coordinate
mac.crop((0,0,100,100))

pencils = Image.open('pencils.jpg')
#pencils.show()
size = pencils.size
x = 0
y = 0
w = size[0]/3
h = size[1]/10

pencils.crop((x,y,w,h))

size = mac.size
half_way = size[0]/2
x = half_way - 200
w = half_way + 200
y = 800
h = size[1]
# Copy
computer = mac.crop((x,y,w,h))
# Paste
mac.paste(im=computer, box=(0,0))
# mac.show()
mac.resize((3000,500))
mac.rotate(90)
red = Image.open('red_color.jpg')
# red.show()
blue = Image.open('blue_color.png')
rgb_im = blue.convert('RGB')
rgb_im.save('blue_color.jpg')
rgb_im.show()
# blue putalpha has an error making it fully black whenever alpha is changed need to make it JPG first
rgb_im.putalpha(120)
red.putalpha(128)
# red.show()
# blue.show()
# mask should be the same as the image
rgb_im.paste(im=red,box=(0,0),mask=red)
rgb_im.show()
rgb_im.save("purple1.png")
