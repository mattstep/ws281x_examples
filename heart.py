import leds

WIDTH     = 8
HEIGHT    = 8
AMPLITUDE = 100

HEART = [[0,1,1,0,0,1,1,0],
         [1,4,4,1,1,4,4,1],
         [4,4,4,4,4,4,4,4],
         [4,4,4,4,4,4,4,4],
         [1,4,4,4,4,4,4,1],
         [0,1,4,4,4,4,1,0],
         [0,0,1,4,4,1,0,0],
         [0,0,0,1,1,0,0,0]]

COLOR = 0x082008

channel, board = leds.initialize(WIDTH, HEIGHT, AMPLITUDE)

try:

  buffer = [[HEART[i][j]*COLOR for j in range(WIDTH)] for i in range(HEIGHT)]
  leds.set(channel, board, buffer) 

finally:
  leds.shutdown(board)
