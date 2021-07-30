from microbit import pin0, pin1
import time
import machine


class HCSR04:
    def __init__(self, tpin=pin0, epin=pin1):
        self.trigger_pin = tpin
        self.echo_pin = epin

    def distance_mm(self):
        self.trigger_pin.write_digital(0)
        time.sleep_us(2)
        # Send the trigger signal for 10 us
        self.trigger_pin.write_digital(1)
        time.sleep_us(10)
        self.trigger_pin.write_digital(0)

        # Returns the duration (us)
        output = machine.time_pulse_us(self.echo_pin, 1)

        dist = output * 0.34 / 2

        return dist
