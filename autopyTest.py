import autopy
import math
import time
import random

TWO_PI = math.pi * 2.0

def sine_mouse_wave():
	"""
	Moves the mouse in a sine wave from the left edge of the screen
	to the right
	"""
	width,height = autopy.screen.get_size()
	height /= 2
	height -= 10 #Stay in the screen bounds.

	for x in xrange(width):
		y = int(height * math.sin((TWO_PI * x) / width) + height)
		autopy.mouse.move(x,y)
		time.sleep(random.uniform(0.001,0.003))



def crazySaveScreenCapture():
	for i in range(0,1000):
		filename = str(i) + '.png'
		autopy.bitmap.capture_screen().save('./test/' + filename)


def where_is_the_monkey():
	monkey = autopy.bitmap.Bitmap.open('monkey.png')
	barrel = autopy.bitmap.Bitmap.open('monkey.png')

	pos = barrel.find_bitmap(monkey)
	if pos:
		print "We found him! he's here: %s" % str(pos)
	else:
		print "There is no monkey... what kind of barrel is this?"


#sine_mouse_wave()
#crazySaveScreenCapture()
where_is_the_monkey()