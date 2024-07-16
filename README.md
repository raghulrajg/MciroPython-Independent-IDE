# MciroPython-Independent-IDE
The MicroPython Web Code Editor eliminates the need for physical IDE software by providing a high-speed program upload to your device. It features an inbuilt web server to host the MicroPython code editor webpage, allowing for seamless uploading, debugging, and more directly through your web browser.

[![micropython](https://img.shields.io/badge/micropython-Ok-purple.svg)](https://micropython.org)

[![ESP8266](https://img.shields.io/badge/ESP-8266-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp8266)

[![ESP32](https://img.shields.io/badge/ESP-32-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp32)
[![ESP32](https://img.shields.io/badge/ESP-32S2-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp32-s2)
[![ESP32](https://img.shields.io/badge/ESP-32C3-000000.svg?longCache=true&style=flat&colorA=CC101F)](https://www.espressif.com/en/products/socs/esp32-c3)

**This works with the ESP8266 Arduino platform**

[https://github.com/esp8266/Arduino](https://github.com/esp8266/Arduino)

**This works with the ESP32 Arduino platform** 

[https://github.com/espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)

## Table of Contents

- [Features](#features)
- [How It Looks](#how-it-looks)
- [Installation](#installation)
- [Usage](#usage)
  - [Setup](#setup)
  - [Upload and Error check](#upload-and-error-check)
- [Important Notes](#important-notes)

## Installation

### Installing with mip

Py-file
```python
import mip
mip.install('github:raghulrajg/MciroPython-Independent-IDE/freeIDE.py')
```

To install using mpremote

```bash
    mpremote mip install github:raghulrajg/micropython-freeIDE
```

To install directly using a WIFI capable board

```bash
    mip.install("github:raghulrajg/micropython-freeIDE")
```

### Installing Library Examples

If you want to install library examples:

```bash
    mpremote mip install github:raghulrajg/micropython-freeIDE/examples.json
```

To install directly using a WIFI capable board

```bash
    mip.install("github:raghulrajg/micropython-freeIDE/examples.json")
```

### Installing from PyPI

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-freeIDE/>`_.
To install for current user:

```bash
    pip3 install micropython-freeIDE
```

To install system-wide (this may be required in some cases):


```bash
sudo pip3 install micropython-freeIDE
```
To install in a virtual environment in your current project:

```bash
    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-freeIDE
```

Also see [examples](https://github.com/raghulrajg/MciroPython-Independent-IDE/tree/main/test).
