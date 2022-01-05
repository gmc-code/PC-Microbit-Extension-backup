# BitBotXL LEDs # rainbow fade in and out
from microbit import *
import neopixel
import math

num_pixels = 12
pin_num = pin13
np = neopixel.NeoPixel(pin_num, num_pixels)

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return (v, v, v)
    i = int(h*6.0)  # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i % 6
    if i == 0:
        return (v, t, p)
    if i == 1:
        return (q, v, p)
    if i == 2:
        return (p, v, t)
    if i == 3:
        return (p, q, v)
    if i == 4:
        return (t, p, v)
    if i == 5:
        return (v, p, q)

def MakeColour(h, brightness):
    brightness = min(255, brightness)
    hsv = hsv_to_rgb(h, 1, 0.5)
    r, g, b = hsv
    return (math.floor(r*brightness), math.floor(g*brightness), math.floor(b*brightness))

def Rainbow(np, brightness):
    for pix in range(num_pixels):
        r, g, b = MakeColour(pix/(num_pixels), brightness)
        np[pix] = (r, g, b)
    np.show()

def Rainbow_fade_in_and_out(np, maxbrightness):
    for i in range(1, maxbrightness, 2):
        Rainbow(np, i)
        sleep(30)
    for i in range(maxbrightness, 1, -2):
        Rainbow(np, i)
        sleep(30)

for x in range(10):
    Rainbow_fade_in_and_out(np, 40)

np.clear()
