import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 16, brightness = 1)

pixels.fill((255, 0, 0))