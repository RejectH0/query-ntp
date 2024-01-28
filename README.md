
# NTP Query Tool

## Overview
This Python program is designed to query a specified Network Time Protocol (NTP) server for the current time. It then converts this time from Coordinated Universal Time (UTC) to a desired timezone. This tool is useful for systems or environments where accurate time synchronization is critical.

## How it Works
- The program creates a UDP socket and sends a request to the specified NTP server.
- The NTP server responds with the current time in UTC.
- The program converts this UTC time to the specified timezone.

## Configuration
To use this program, you need to modify the following variables in the `query.ntp.py` script:

- `NTP_SERVER`: The hostname or IP address of the NTP server you wish to query.
- `NTP_PORT`: The port on which the NTP server is listening (default is 123, the standard NTP port).
- `TIMEZONE`: The desired timezone to which you want to convert the UTC time. This should be a valid timezone string (e.g., 'America/New_York', 'Europe/Berlin').

## Usage
1. Ensure you have Python 3 installed on your system.
2. Modify the `NTP_SERVER` and `TIMEZONE` variables in the script to suit your requirements.
3. Run the script: `python3 query.ntp.py`

## Dependencies
- Python 3.x
- The `socket` and `struct` modules for network communication and data structure handling, respectively.
- The `datetime` and `zoneinfo` modules for time manipulation and timezone conversions.

## Error Handling
The program includes basic error handling to manage issues such as network errors or invalid server responses.

## Note
- This script is intended for educational or development purposes and should be tested thoroughly before use in a production environment.
- Ensure that the NTP server you are querying permits such requests and that you comply with any usage policies.

## Credits
- Thanks to ChatGPT for the creation of this README.md file, as well as supporting programming assistance with the underlying Python3 code.
