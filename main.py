# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyfirmata
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



def control_arduino():
    a = pyfirmata.Arduino("COM4", baudrate=57600)  # Baudrate must match rate set in sketch
    # time.sleep(3)
    a.pin_mode(12, pyfirmata.OUTPUT)

    print("wait")
    time.sleep(2)
    print("Go")
    b = 1
    while True:
        a.digital[12].write(1)
        time.sleep(1)
        a.digital[12].write(0)
        time.sleep(1)
    #     a.digital_write(12, pyfirmata.HIGH)
    #     time.sleep(1)
    #     a.digital_write(12, pyfirmata.LOW)
    #     time.sleep(1)
    #     print("count", b)
    #     b = b + 1
    # # a.serial.close()
