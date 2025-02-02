from bodies.common import *

class Satellite(Body):
	def __init__(self, mass=1, starting_x=10, starting_y=10, starting_speed_x=0.0, starting_speed_y=0.0, starting_acceleration_x=0.0, starting_acceleration_y=0.0, base_oom=10**8):
		super().__init__(mass / base_oom, starting_x, starting_y, starting_speed_x, starting_speed_y, starting_acceleration_x, starting_acceleration_y)
		self.body_name = "satellite"

		self.base_oom = base_oom
		self.setRadius(mass / 10)
		self.base_color_name = "gray"
		self.color(self.base_color_name)