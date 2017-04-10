class Cuboid(object):

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_surface(self):
        surface = 2 * (self.width * self.height + self.width * self.depth + self.height * self.depth)
        return surface

    def get_volume(self):
        volume = self.width * self.height * self.depth
        return volume

    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
