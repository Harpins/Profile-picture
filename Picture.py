from PIL import Image
image=Image.open("image.jpg")
red, green, blue = image.split()
width_diff=100
height_diff=50
red_crop=red.crop((width_diff, height_diff, red.width, red.height))
blue_crop=blue.crop((0, 0, blue.width-width_diff, blue.height-height_diff))
green_crop=green.crop((width_diff//2, height_diff//2, green.width-width_diff//2, green.height-height_diff//2))
image_merged=Image.merge("RGB", (red_crop, green_crop, blue_crop))
image_merged.save("new_image.jpg")
image_merged.thumbnail((80,80))
image_merged.save("small_image.jpg")


