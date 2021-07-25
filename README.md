# Introduction

Controlling of SPI type LED strips, mostly made of API102 chips, using GPIO ZERO.
Original version of the code was appeared here [(GitHub Issue: Add SPI output support for API102 LEDs)](https://github.com/gpiozero/gpiozero/issues/551)

# pinout

| Raspberry Pi   | SPI       | APA102 |
|----------------|-----------|--------|
| GPIO10 (Pin19) | SPI_MOSI  | SDI    |
| GPIO11 (Pin32) | SPI_SCLK  | CLK    |
| 5V0            | VDD_5V    | VDD    |

