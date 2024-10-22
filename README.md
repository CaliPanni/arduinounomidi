# arduinounomidi
Use an arduino uno as midi device
&nbsp;
##requirements:
* Breadboard;
* 2 20k 3 pin potentiometers;
* 2 Smd buttons;
* Arduino Uno;
* 2 10kohms resistors;
* 9 Jumper files M-M;
* Arduino IDE ([Download](https://www.arduino.cc/en/software));
* Python ([Download](https://www.python.org/downloads/));
* LoopMIDI ([Download](https://www.tobias-erichsen.de/software/loopmidi.html)).
##Setup:
&nbsp;
1. Install python **ALSO ON PATH**, arduino IDE, LoopMIDI and restart the pc.
2. Download the source code and extract it.
3. Run the command prompt on the source code dir and type:
 ```
pip install -r requirements.txt

```
4. Create new virtual midi port with LoopMIDI.
5. Open midi.ino and Flash it into the Arduino uno board.
6. Disconnect the board and make connections as in the photo:
   ![connections](https://github.com/CaliPanni/arduinounomidi/blob/main/circuito_potenziometro.png?raw=true)
7. Edit *serial2midi.py* with the Arduino com port and the name of the virtual midi port.
  *If you don't know the name of the midi port, double click on* `getmidi.py`.
  ![getmidy.py](https://github.com/CaliPanni/arduinounomidi/blob/main/getmidi.png?raw=true)
8. Run the command prompt on the source code dir and type:
 ```
python serial2midi.py

```
or just dubleclick it.
9. Map the midi to the program you want to use.
10. Enjoy!
