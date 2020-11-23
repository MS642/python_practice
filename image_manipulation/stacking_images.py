from PIL import Image
table = Image.open('word_matrix.png')
mask = Image.open('mask.png')

mask.putalpha(128)
# resize doesnt change the original, but returns a new image with the new size
mask = mask.resize(table.size)
mask.show()
table.show()
table.paste(im=mask,box=(0,0),mask=mask)

table.show()