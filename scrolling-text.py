import time
import leds
import math
import struct
from PIL import Image, ImageDraw, ImageFont

WIDTH     = 8
HEIGHT    = 8
AMPLITUDE = 100
MESSAGE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
FONT = '/usr/share/fonts/truetype/droid/DroidSans.ttf'


channel, board = leds.initialize(WIDTH, HEIGHT, AMPLITUDE)

imageWidth = WIDTH*20
image = Image.new("RGB", (imageWidth,HEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(FONT, 8)

draw.text((0, 0), MESSAGE, (50,50,50), font=font)

raw = image.tobytes()

packed = [[struct.unpack('>I', b'\x00'+raw[(i + j*imageWidth) * 3 : (i + j*imageWidth + 1) * 3 ])[0] for i in range(imageWidth) ] for j in range(HEIGHT)]

try:

  for k in range(imageWidth-WIDTH+1):
    buffer = [[packed[i][j+k] for j in range(WIDTH)] for i in range(HEIGHT)]
    leds.set(channel, board, buffer) 
    time.sleep(0.1)


finally:
  leds.shutdown(board)
