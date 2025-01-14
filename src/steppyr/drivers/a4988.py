from .stepdir import StepDirDriver
import RPi.GPIO as GPIO

class A4988Driver(StepDirDriver):
  """
  The A4988 provides a STEP/DIR interface and allows setting microstep
  resolution with the ms* pins.
  """

  microstep_table = {
    0: int('000', 2),
    1: int('000', 2),
    2: int('001', 2),
    4: int('010', 2),
    8: int('011', 2),
    16: int('111', 2) }
  # tA STEP minimum, HIGH pulse width (1us)
  step_high_min_us = 1;
  # tB STEP minimum, LOW pulse width (1us)
  step_low_min_us = 1;
  # wakeup time, nSLEEP inactive to STEP (1000us)
  wakeup_time_us = 1000;
  #also 200ns between ENBL/DIR/MSx changes and STEP HIGH

  def __init__(self, dir_pin, step_pin, enable_pin=None, pin_mode=GPIO.BCM,
               ms1_pin=None, ms2_pin=None, ms3_pin=None):
    super().__init__(dir_pin, step_pin, enable_pin, pin_mode)
    self.ms3_pin = ms3_pin
    self.ms2_pin = ms2_pin
    self.ms1_pin = ms1_pin

  def activate(self):
    super().activate()
    GPIO.setup(self.ms1_pin, GPIO.OUT)
    GPIO.setup(self.ms2_pin, GPIO.OUT)
    GPIO.setup(self.ms3_pin, GPIO.OUT)

  def set_microsteps(self, microsteps):
    super().set_microsteps(microsteps)
    mask = self.microstep_table[microsteps]
    GPIO.output(self.ms3_pin, GPIO.LOW if (mask & 4) == 0 else GPIO.HIGH)
    GPIO.output(self.ms2_pin, GPIO.LOW if (mask & 2) == 0 else GPIO.HIGH)
    GPIO.output(self.ms1_pin, GPIO.LOW if (mask & 1) == 0 else GPIO.HIGH)
