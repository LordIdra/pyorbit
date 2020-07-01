from tkinter import *
from math import *
from time import sleep

def convert(rgb):
	return "#%02x%02x%02x" % (rgb[0], rgb[1], rgb[2])

window = Tk()
window.title('Orbits')

planets = []
ships = []

c = Canvas(width = 600, height = 600, bg = 'black')
c.pack()

grav_const = 6.67408 * (10**-11)

sun_mass = 1.989 * (10**30)
mercury_mass = 0.33011 * (10**24)
venus_mass = 4.8675	* (10**24)
earth_mass = 5.972 * (10**24)
moon_mass = 0.07346 * (24**1)

speed = 100000
divisor = 1000000000

class planet:

	def __init__(self, x, y, mass, colour):

		self.x = x
		self.y = y
		self.mass = mass
		self.acceleration = [0, 0]
		self.initial_momentum = [0, 0]
		self.colour = convert(colour)
		self.rgb = colour
		self.trail = []

		self.rep = c.create_oval(x-5, y-5, x+5, y+5, fill = self.colour, outline = self.colour)

	def tick(self):

		force_vector = [0, 0]

		for pl in planets:

			if pl != self:

				distance = (sqrt(((pl.x-self.x)**2) + ((pl.y-self.y)**2)))
				ac = ((grav_const * pl.mass) / (distance**3))

				force_vector[0] += ((pl.x-self.x) * ac)*speed
				force_vector[1] += ((pl.y-self.y) * ac)*speed

		self.acceleration[0] += force_vector[0]
		self.acceleration[1] += force_vector[1]

		self.x += self.acceleration[0]*speed
		self.y += self.acceleration[1]*speed

		c.delete(self.rep)

		self.trail.append(c.create_oval((self.x/divisor)+295, (self.y/divisor)+295, (self.x/divisor)+305, (self.y/divisor)+305, fill = self.colour, outline = self.colour))

		if len(self.trail) > 100:
			c.delete(self.trail[0])
			self.trail.pop(0)

		for n in range(len(self.trail)):
			col = convert([int(n/self.rgb[0]), int(n/self.rgb[1]), int(n/self.rgb[2])])
			c.itemconfig(self.trail[n], fill = col)
			c.itemconfig(self.trail[n], outline = col)

#Sun at centre of system
planets.append(planet(0, 0, sun_mass, [1, 1, 255]))

#Mercury
planets.append(planet(69.82*(10**9), 0, mercury_mass, [2, 2, 2]))
planets[1].acceleration = [0, 38860]

#Venus
planets.append(planet(108.94*(10**9), 0, venus_mass, [1, 2, 255]))
planets[2].acceleration = [0, 34790]

#Earth and moon
planets.append(planet(152.10*(10**9), 0, earth_mass, [255, 255, 1]))
planets[3].acceleration = [0, 29290]

#planets.append(planet(152.10*(10**9)+406700000, 0, moon_mass, [255, 1, 1]))
#planets[4].acceleration = [0, 29290]


window.update()

while True:
	for pl in planets:
		pl.tick()
	window.update()