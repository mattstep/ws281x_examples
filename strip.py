import time
import leds

LENGTH    = 288
AMPLITUDE = 255 
DELAY     = 0.003
BASECOLOR = 0x788070

CYCLE     = [0x8080FF, 0x80FFFF, 0x80FF80, 0xFFFF80, 0xFF8080, 0xFF80FF]
DECAY     = 0.99

def dim(i,j):
  b = i & 0x0000FF
  r = (i & 0x00FF00) >> 8
  g = (i & 0xFF0000) >> 16
  return (int(g*j) << 16) + (int(r*j) << 8) + int(b*j)

def amplitude(i):
  b = i & 0x0000FF
  r = (i & 0x00FF00) >> 8
  g = (i & 0xFF0000) >> 16
  return b+g+r

def sum(i,j):
  b1 = i & 0x0000FF
  r1 = (i & 0x00FF00) >> 8
  g1 = (i & 0xFF0000) >> 16
  b2 = j & 0x0000FF
  r2 = (j & 0x00FF00) >> 8
  g2 = (j & 0xFF0000) >> 16
  return (min(255,g1+g2) << 16) + (min(255,r1+r2) << 8) + min(255,b1+b2)

def dif(i,j):
  b1 = i & 0x0000FF
  r1 = (i & 0x00FF00) >> 8
  g1 = (i & 0xFF0000) >> 16
  b2 = j & 0x0000FF
  r2 = (j & 0x00FF00) >> 8
  g2 = (j & 0xFF0000) >> 16
  return (max(0,g2-g1) << 16) + (max(0,r2-r1) << 8) + max(0,b2-b1)

channel, board = leds.initialize(1, LENGTH, AMPLITUDE)

try:

  colors = [BASECOLOR for i in range(LENGTH)]
  
  leds.set(channel, board, colors)

  i = 0
  j = 0
  d = 1
  while True:
    colors[i] = CYCLE[j]
    leds.set(channel, board, colors)
    time.sleep(DELAY)
    for k in range(LENGTH):
      colors[k] = dim(colors[k],DECAY)
      if amplitude(colors[k]) < amplitude(BASECOLOR):
        colors[k] = dim(sum(BASECOLOR,colors[k]),0.5)
    i = i + d
    if i >= LENGTH or i < 0:
      j += 1
      d = d * -1
      i = i + d
    if j >= len(CYCLE):
      j = 0

finally:
  leds.shutdown(board)
