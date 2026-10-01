import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac_pins=[22,27,17,26,25,21,20,16]
GPIO.setup(dac_pins, GPIO.OUT)
dynamic_range=3.3
def voltage_to_number(voltage):
    if not (0.0<=voltage<=dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int((voltage/dynamic_range)*255)
def number_to_dac(number):
    bin_string=bin(number)[2:].zfill(8)
    bin_bits=[int(bit) for bit in bin_string[::-1]]
    GPIO.output(dac_pins,bin_bits)
try:
    while True:
        try:
            voltage=float(input("Введите напряжение в Вольтах: "))
            number=voltage_to_number(voltage)
            number_to_dac(number)
            bin_string=bin(number)[2:].zfill(8)
            display_bits=[int(bit) for bit in bin_string]
            print(f"Число на вход ЦАП: {number}, биты: {display_bits}")
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    GPIO.output(dac_pins,0)
    GPIO.cleanup()