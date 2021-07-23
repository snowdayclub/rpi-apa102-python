import time

from gpiozero import SPIDevice

class Apa102Pixel(SPIDevice):
    def __init__(self, *args, **kwargs):
        super(Apa102Pixel, self).__init__(*args, **kwargs)
        self._brightness = 255.0
        self._value = (0, 0, 0)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        r, g, b = [int(self._brightness * v) for v in value]
        data = [0]*4 + [0b11100000 | 31, b, g, r] + [0]*5
        self._spi.transfer(data)
        self._value = value

    def on(self):
        self.value = (1, 1, 1)

    def off(self):
        self.value = (0, 0, 0)

    def close(self):
        self.off()
        super(Apa102Pixel, self).close()

class Apa102PixelStrip(SPIDevice):
    def __init__(self, pixels, *args, **kwargs):
        super(Apa102PixelStrip, self).__init__(*args, **kwargs)
        self._brightness = 255.0
        self._pixels = pixels
        self.off()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        start_of_frame = [0]*4
        end_of_frame = [0]*5
        start_of_pixel = 0b11100000 | 31 # Start bits and 5-bit brightness (0-31)
        pixels = [[int(self._brightness*v) for v in p] for p in value]
        pixels = [[start_of_pixel, b, g, r] for r, g, b in pixels]
        pixels = [i for p in pixels for i in p]
        data = start_of_frame + pixels + end_of_frame
        self._spi.transfer(data)
        self._value = value

    def on(self):
        self.value = ((1, 1, 1),) * self._pixels

    def off(self):
        self.value = ((0, 0, 0),) * self._pixels

    def close(self):
        self.off()
        super(Apa102PixelStrip, self).close()


'''
# As a strip
blinkt = Apa102PixelStrip(8, mosi_pin=23, clock_pin=24)

for colour in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
    blinkt.value = [colour] * 8
    time.sleep(1)


# As a single LED
blinkt = Apa102Pixel(mosi_pin=23, clock_pin=24)

for colour in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
    blinkt.value = colour
    time.sleep(1)

'''
