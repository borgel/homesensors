# Setup
Flash micropython to the ESP8266 following [the guide](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html).

Setup dev machine:
```bash
brew install picocom micropython
pip3 install adafruit-ampy
```

Update your wifi credentials in `boot.py`.

Ask your local `git` to ignore chances to this file with `git update-index --assume-unchanged boot.py` so it doesn't prompt you to commit your wifi credentials.

Send the code to the micro:
```bash
./do-flash boot.py
```

Open a REPL on device (perhaps with `do-picocom.sh`?) and install dependencies on device:
```python
import upip
upip.install("urequests")
```

Install the application on device
```bash
./do-flash.sh main.py
```

Plug it in wherever it will run!

# Usage
Haha todo


# For Reference
Default boot.py that came with micopython:
```python
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
```

