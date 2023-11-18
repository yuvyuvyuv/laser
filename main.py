# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyfirmata
import time
import keyboard  # using module keyboard
import main
import laser_get
import get_range


center_of_frame_x = 320

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main.run_scan()
    # a = main.start_arduino()
    # main.start_laser_arduino(a)


def run_scan():
    point = [0, 0]
    arduino = main.start_arduino()
    # main.stop_laser_arduino(arduino)
    # time.sleep(5)
    vid = laser_get.start_video_capture()
    # time.sleep(4)
    # main.stop_laser_arduino(arduino)
    print("Press a key to start:")
    while True:
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print("Got q key!")
                main.start_laser_arduino(arduino)
                point = laser_get.display_stream_and_calculate_light(vid)
                print("point is: ", point)
                break
            elif keyboard.is_pressed('s'):
                print('Finished')
            else:
                continue
        except:
            break  # if user pressed a key other than the given key the loop will break
    final_dist = get_range.get_range(320, point[0])
    print("distance to wall, from camera, is: ", final_dist)


def start_arduino():
    a = pyfirmata.Arduino("COM4")  # Baudrate must match rate set in sketch
    print("started")
    # a.digital[13].write(1)
    return a


def stop_laser_arduino(arduino):
    # a = pyfirmata.Arduino("COM4")  # Baudrate must match rate set in sketch
    print("stopped")
    arduino.digital[13].write(0)


def start_laser_arduino(arduino):
    # a = pyfirmata.Arduino("COM4")  # Baudrate must match rate set in sketch
    print("started")
    arduino.digital[13].write(1)


def control_arduino():
    a = pyfirmata.Arduino("COM4")  # Baudrate must match rate set in sketch
    print("started")
    # a.digital[13].write(1)
    # time.sleep(1)
    # time.sleep(3)
    # a.pin_mode(13, pyfirmata.OUTPUT)

    # print("wait")
    # time.sleep(2)
    # print("Go")
    # b = 1
    while True:
        # time.sleep(1)
        #     print("started")
        a.digital[13].write(1)
        time.sleep(1)
        a.digital[13].write(0)
        time.sleep(1)
    #     a.digital_write(12, pyfirmata.HIGH)
    #     time.sleep(1)
    #     a.digital_write(12, pyfirmata.LOW)
    #     time.sleep(1)
    #     print("count", b)
    #     b = b + 1
    # # a.serial.close()


# def get_press_from