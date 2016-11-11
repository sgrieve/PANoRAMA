import Image
from images2gif import writeGif


a = Image.open('/home/sgrieve/Pictures/pano.png')

step = 10

w, h = a.size
final_width = int(h * 1.5)

images = []

for i in range(0, w - final_width, step):
    images.append(a.crop((i, 0, final_width + i, h)))

for i in range(w - final_width, 0, -step):
    images.append(a.crop((i, 0, final_width + i, h)))


for b, j in enumerate(images):
    j.save('/home/sgrieve/Pictures/tmp/' + str(b).zfill(4) + '.png')
