#!/usr/bin/python3
from gpiozero import SPIDevice

class SpiLedStrip(SPIDevice):
    def __init__(self, pixels, *args, **kwargs):
        super(SpiLedStrip, self).__init__(*args, **kwargs)
        self._pixels = pixels
        self._start_of_frame = [0] * 4
        # at least one bit of clock is required for every 2 leds
        self._end_of_frame = [255] * int(self._pixels/2/8 + 1)
        # global brightness is fixed
        self._brightness =  0b11111111;
        self.off()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        pixels = [[self._brightness, b&0xff, g&0xff, r&0xff] for r, g, b in value]
        pixels = [y for x in pixels for y in x]
        data = self._start_of_frame + pixels + self._end_of_frame
        self._spi.transfer(data)
        self._value = value

    def on(self):
        self.value = ((255, 255, 255),) * self._pixels

    def off(self):
        self.value = ((0, 0, 0),) * self._pixels


if __name__=='__main__':
    import time
    # create an instance: 3 leds, hardware SPI
    strip = SpiLedStrip(3, clock_pin=11, mosi_pin=10)
    # pixel map squence: list of (r,g,b) values
    pixels_seq = [
            [(255,0,0),(0,0,0),(0,0,0)],       # The first LED is set to RED
            [(0,0,0),(0,255,0),(0,0,0)],       # Then the second to GREEN
            [(0,0,0),(0,0,0),(0,0,255)] ]      # Finally the last one to BLUE

    for pixels in pixels_seq:
        strip.value = pixels
        time.sleep(1)

    # turn off the strip
    strip.off()

