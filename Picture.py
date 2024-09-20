from PIL import Image
image=Image.open("image.jpg")
red, green, blue = image.split()
width_diff=50
height_diff=0

red_left=red.crop((width_diff, height_diff, red.width, red.height))
red_center=red.crop((width_diff//2, height_diff//2, red.width-width_diff//2, red.height-height_diff//2))
red_shift=Image.blend(red_left, red_center, 0.2)

blue_right=blue.crop((0, 0, blue.width-width_diff, blue.height-height_diff))
blue_center=blue.crop((width_diff//2, height_diff//2, blue.width-width_diff//2, blue.height-height_diff//2))
blue_shift=Image.blend(blue_right, blue_center, 0.2)

green_crop=green.crop((width_diff//2, height_diff//2, green.width-width_diff//2, green.height-height_diff//2))
image_merged=Image.merge("RGB", (red_shift, green_crop, blue_shift))
image_merged.save("new_image.jpg")
image_merged.thumbnail((80,80))
image_merged.save("small_image.jpg")


