# Router password Changer

## Overview

Change your `Tecno` router password right from your terminal.

## Description

Some internet providers block the ssh/telnet from their routers. making it harder for developers to administer their network. The point of this tool is to **avoid using the provided Http GUI** by directly interacting with the internal API of the router, while still maintaining the same level of security.

This has been tested on a `4G Tecno router`

## General flow

This represents the general flow of this script, following the router flow.

```mermaid
sequenceDiagram
    participant Client Side
    participant Server Side
    Client Side->>Server Side: getRandomLogin()
    Server Side->>Client Side: { random_login }
    Client Side->>Server Side: login: base64(username), base64(sha256(random_login+pass))
    Server Side->>Client Side: { result, power, cookie }
    Client Side->>Client Side: random = SHA256(cookie)
	Client Side->>Server Side: get_token(headers=Cookie{random})
	Server Side->>Client Side: { token }
	Client Side->>Server Side: set_wifi_settings( { csrf=sha256(token), ...params }, headers=Cookie{random})
```

## Todo 

- Add a QR Code generator
- Change the device's wifi password automatically after a successfull passphrase modification