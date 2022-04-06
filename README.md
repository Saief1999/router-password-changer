# Router password Changer

## Overview

Change your `Tecno` router password right from your terminal.

## Description

Some internet providers block the ssh/telnet ports from their routers. making it harder for developers to administer their network. The point of this tool is to **avoid using the provided Http GUI** by directly interacting with the internal API of the router, while still maintaining the same level of security.

This has been tested on a `4G Tecno router`

## Requirements

Install all requirements by running : 

```bash
pip install -r requirements.txt
```
## Usage 

**Note**: You need to be connected to the wifi network of the router to use this tool.

```bash
```
usage: password_changer.py [-h] [-pp PASSPHRASE] [-a ADMIN] [-p PASSWORD] ssid

positional arguments:
  ssid                  Wifi name.

options:
  -h, --help            show this help message and exit
  -pp PASSPHRASE, --passphrase PASSPHRASE
                        Wifi passphrase (default: randomly generated password)
  -a ADMIN, --admin ADMIN
                        Admin account login. (default: admin)
  -p PASSWORD, --password PASSWORD
                        Admin account password. (default: admin)

```
## General flow

This represents the general flow of this script, following the router flow.

```mermaid
sequenceDiagram
    participant Client Side
    participant Server Side
    Client Side->>Server Side: POST: get_random_login()
    Server Side->>Client Side: { random_login }
    Client Side->>Server Side: POST: login -  base64(username), base64(sha256(random_login+pass))
    Server Side->>Client Side: { result, power, cookie }
    Client Side->>Client Side: random = SHA256(cookie)
	Client Side->>Server Side: GET: get_token(headers=Cookie{random})
	Server Side->>Client Side: { token }
	Client Side->>Server Side: POST: set_wifi_settings( { csrf=sha256(token), ...params }, headers=Cookie{random})
```

## Todo 

- Add a QR Code generator
- Change the device's wifi password automatically after a successfull passphrase modification
