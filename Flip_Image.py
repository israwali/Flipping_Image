
#FLipping the image
from PIL import Image

#opening the image
img=Image.open('C:\\Users\\Isra\\Documents\\Coding\\Python\\evidence-board.png')

#transposing 
transposed_img=img.transposed(Image.FLIP_LEFT_RIGHT)

#save it to a file ina human understandable format
transposed_img.save('C:\\Users\\Isra\\Documents\\Coding\\Python\\corrected.png')

print('Done flipping')

