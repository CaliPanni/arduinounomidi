import mido
import serial
import time
serial_port = 'COM3'  # edit this with the arduino com port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
midi_out = mido.open_output('arduino 1') # edit this with your virtual midi port name
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
last_midi_value1 = -1
last_midi_value2 = -1
last_button1_state = 0
last_button2_state = 0
try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        pot1, pot2, button1, button2 = line.split(',')
        pot1 = int(pot1)
        pot2 = int(pot2)
        button1 = int(button1)
        button2 = int(button2)
        midi_value1 = map_value(pot1, 0, 1023, 0, 127)
        midi_value2 = map_value(pot2, 0, 1023, 0, 127)
        if abs(midi_value1 - last_midi_value1) > 2: 
            midi_out.send(mido.Message('control_change', channel=0, control=1, value=midi_value1))  
            last_midi_value1 = midi_value1
        if abs(midi_value2 - last_midi_value2) > 2: 
            midi_out.send(mido.Message('control_change', channel=0, control=2, value=midi_value2))  
            last_midi_value2 = midi_value2
        if button1 == 1 and last_button1_state == 0:  
            midi_out.send(mido.Message('note_on', note=84, velocity=127))  #C5
            last_button1_state = 1 
        if button1 == 0 and last_button1_state == 1:  
            midi_out.send(mido.Message('note_off', note=84, velocity=0))
            last_button1_state = 0 
        if button2 == 1 and last_button2_state == 0: 
            midi_out.send(mido.Message('note_on', note=86, velocity=127))  #D5
            last_button2_state = 1  
        if button2 == 0 and last_button2_state == 1: 
            midi_out.send(mido.Message('note_off', note=86, velocity=0))
            last_button2_state = 0  
except KeyboardInterrupt:
    print("program stopped with CTRL + C.")
finally:
    ser.close()
    midi_out.close()
