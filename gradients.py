import time
import leds

WIDTH     = 8
HEIGHT    = 8
AMPLITUDE = 50
DELAY     = 1

channel, board = leds.initialize(WIDTH, HEIGHT, AMPLITUDE)

try:

  colors = [[0 for i in range(HEIGHT)] for j in range(WIDTH)]

  for i in range(WIDTH):
    for j in range(HEIGHT):
      colors[i][j] = ((i << 4) << 8) + (j << 4)

  leds.set(channel, board, colors)
  
  time.sleep(DELAY)

  for i in range(WIDTH):
    for j in range(HEIGHT):
      colors[i][j] = ((i << 4) << 16) + (j << 4)

  leds.set(channel, board, colors)

  time.sleep(DELAY)

  for i in range(WIDTH):
    for j in range(HEIGHT):
      colors[i][j] = ((i << 4) << 8) + ((j << 4) << 16)

  leds.set(channel, board, colors)

finally:
  leds.shutdown(board)
