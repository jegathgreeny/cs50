from PIL import Image, ImageOps

shirt = Image.open('shirt.png')
size = shirt.size


photo = Image.open('before1.jpg')
photo = ImageOps.fit(photo, size)

photo.paste(shirt, shirt)
photo.save('another.jpg')

print(photo)
