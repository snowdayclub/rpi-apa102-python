# Introduction

Controlling of SPI type LED strips, mostly made of API102 chips, using GPIO ZERO.
Original version of the code was appeared in [1](https://github.com/gpiozero/gpiozero/issues/551).
And detailed information about the protocol can be found in [2](https://cpldcpu.wordpress.com/2014/11/30/understanding-the-apa102-superled/).

# Pinout

| Raspberry Pi   | SPI       | APA102 |
|----------------|-----------|--------|
| GPIO10 (Pin19) | SPI_MOSI  | SDI    |
| GPIO11 (Pin32) | SPI_SCLK  | CLK    |
| 5V0            | VDD_5V    | VDD    |

# References

1. [GitHub Issue: Add SPI output support for API102 LEDs](https://github.com/gpiozero/gpiozero/issues/551)
2. [Understanding the APA102 "Superled"](https://cpldcpu.wordpress.com/2014/11/30/understanding-the-apa102-superled/)
