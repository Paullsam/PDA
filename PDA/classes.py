class Robot:

    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        return self._power

walle = Robot(300)
print(walle.power)
