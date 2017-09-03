from PIL import Image

a = Image.open('input.jpg')

step = 100

w, h = a.size
final_width = int(h * 1.5)
images = []

for i in range(0, w - final_width, step):
    images.append(a.crop((i, 0, final_width + i, h)))

# This leaves a black screen at the end of each loop
# images = images + images[::-1]

# This second loop should be replaced by the slicing above
for i in range(w - final_width, 0, -step):
    images.append(a.crop((i, 0, final_width + i, h)))

output = Image.new(a.mode, (final_width, h))
output.save('hello.gif', save_all=True, append_images=images, duration=200,
            loop=0)
