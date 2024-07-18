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
- [Setup Your Development Environment](#setup-your-development-environment)
- [Installation](#installation)
- [Usage](#usage)
  - [Setup](#setup)
  - [Upload and Error check](#upload-and-error-check)
- [Important Notes](#important-notes)

## Setup Your Development Environment

To set up your development environment, follow these steps:

1. **Install MicroPython on Your Board:**

    - Download the latest MicroPython firmware for your board from the [official MicroPython website](https://micropython.org/download/).
    - Flash the firmware to your board using a tool like `esptool.py`:

      ```sh
      esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
      esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin
      ```

      Replace `/dev/ttyUSB0` with the appropriate port for your system and `esp32-20220117-v1.18.bin` with the firmware file you downloaded.

2. **Install `ampy`:**

    `ampy` is a command-line tool to interact with a MicroPython board over a serial connection.

    ```sh
    pip install adafruit-ampy
    ```

3. **Connect to Your Board:**

    Ensure your board is connected to your computer via a USB cable. Identify the serial port used by your board. On Unix-based systems (Linux/macOS), it might be something like `/dev/ttyUSB0`, and on Windows, it might be `COM3` or similar.

4. **Upload Files to Your Board:**

    Use `ampy` to upload files to your MicroPython board. For example, to upload a file named `main.py`:

    ```sh
    ampy --port /dev/ttyUSB0 put main.py
    ```

    Replace `/dev/ttyUSB0` with the appropriate serial port for your setup.

5. **Run Scripts on Your Board:**

    To run a script directly on your MicroPython board, use the `run` command:

    ```sh
    ampy --port /dev/ttyUSB0 run main.py
    ```

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

## Usage

## Upload and Error check

### MicroPython Web Code Editor
The purpose of the MicroPython web code editor is to eliminate the need for physical IDE software. This web editor provides a high-speed program upload to the device and includes an inbuilt web server to host the MicroPython code editor webpage. It can handle uploading, debugging, and more.

### Editor Options
The editor has two buttons: 'Run' and 'Status'

`Run`: This button uploads the program to the corresponding device and checks for syntax errors only. Once the program is uploaded, wait a few seconds until the device's onboard LED turns off.
`Status`: This button checks for error logs. If the previously uploaded program has runtime errors, they will be notified here.

### Shortcut Keys
`Ctrl+u`, `F4`: Upload the program.

`F2`: Check for error logs.
