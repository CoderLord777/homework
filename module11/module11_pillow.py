from PIL import Image, ImageFilter

image = Image.open("image_module11.jpg")

image.show()
new_image = image.resize((300, 300))
new_image.show()
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()
cut = image.crop((200, 100, 300, 300))
cut.show()
image.save("example_new.png", "PNG")
