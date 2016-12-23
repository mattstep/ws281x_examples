import time
import leds
import math

WIDTH     = 8
HEIGHT    = 8
AMPLITUDE = 50
DELAY     = 1

channel, board = leds.initialize(WIDTH, HEIGHT, AMPLITUDE)

try:

  colors = [[0 for i in range(HEIGHT)] for j in range(WIDTH)]

  for k in range(20):
    position = 1
    for i in range(WIDTH):
      for j in range(HEIGHT):
        x = i - WIDTH/2
        y = j - WIDTH/2
        r2 = x*x + y*y
        if r2 - 1 <= k and r2 + 1 >= k: 
          colors[i][j] = ((position & 0x1) << 4) + ((position & 0x2) << 12) + ((position & 0x4) << 20)
          position += 1
          if position == 8:
            position = 1
        else:
          colors[i][j] = 0

    leds.set(channel, board, colors)
    time.sleep(0.05)

  leds.clear(channel, board)

finally:
  leds.shutdown(board)
