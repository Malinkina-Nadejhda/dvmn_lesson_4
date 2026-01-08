from PIL import Image

image = Image.open(r"D:\Pyton project\picture\monro.jpg")
rgb_image = image.convert('RGB')
red_channel, green_channel, blue_channel = rgb_image.split()
crop_size = 50
crop_size_2 = crop_size / 2

up_blend_img = red_channel.crop((crop_size, 0, red_channel.width, red_channel.height))
under_blend_img = red_channel.crop((crop_size_2, 0, red_channel.width - crop_size_2, red_channel.height))
red_filter = Image.blend(up_blend_img, under_blend_img, 0.3)

up_blend_img2 = blue_channel.crop((0, 0, blue_channel.width - crop_size, blue_channel.height))
under_blend_img2 = blue_channel.crop((crop_size_2, 0, blue_channel.width - crop_size_2, blue_channel.height))
blue_filter = Image.blend(up_blend_img2, under_blend_img2, 0.3)

green_filter = green_channel.crop((crop_size_2, 0, green_channel.width - crop_size_2, green_channel.height))

final_img = Image.merge("RGB", (red_filter, green_filter, blue_filter))
final_img.thumbnail((80, 80))
final_img.save(r"D:\Pyton project\picture\monroe_filter.jpg")

