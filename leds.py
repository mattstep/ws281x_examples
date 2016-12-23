import time
import _rpi_ws281x as ws
import ctypes

def initialize(width, height, amplitude):
  leds = ws.new_ws2811_t()
  for channum in range(2):
    channel = ws.ws2811_channel_get(leds, channum)
    ws.ws2811_channel_t_count_set(channel, 0)
    ws.ws2811_channel_t_gpionum_set(channel, 0)
    ws.ws2811_channel_t_invert_set(channel, 0)
    ws.ws2811_channel_t_brightness_set(channel, 0)

  channel = ws.ws2811_channel_get(leds, 0)

  ws.ws2811_channel_t_count_set(channel, width*height)
  ws.ws2811_channel_t_gpionum_set(channel, 18)
  ws.ws2811_channel_t_invert_set(channel, 0)
  ws.ws2811_channel_t_brightness_set(channel, amplitude)
  ws.ws2811_t_freq_set(leds, 800000)
  ws.ws2811_t_dmanum_set(leds, 5)

  resp = ws.ws2811_init(leds)
  if resp != ws.WS2811_SUCCESS:
    message = ws.ws2811_get_return_t_str(resp)
    raise RuntimeError('ws2811_init failed : {0} ({1})'.format(resp, message))

  return (channel, leds)

def set(channel, leds, colorArray):
  position = 0
  for row in colorArray:
    for element in row:
      ws.ws2811_led_set(channel, position, ctypes.c_uint32(element).value)
      position += 1

  resp = ws.ws2811_render(leds)
  if resp != ws.WS2811_SUCCESS:
    message = ws.ws2811_get_return_t_str(resp)
    raise RuntimeError('ws2811_render failed : {0} ({1})'.format(resp, message))

def clear(channel, leds):
  set(channel, leds, [[0 for i in range(100)] for j in range(100)])

def shutdown(leds):
  ws.ws2811_fini(leds)
  ws.delete_ws2811_t(leds)
