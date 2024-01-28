#!/usr/bin/python3
import socket
import struct
import sys
import datetime
import zoneinfo

# Constants
NTP_SERVER = 'kronos.sperling.int'  # Replace with your NTP server hostname
NTP_PORT = 123  # Standard NTP port
TIME1970 = 2208988800  # Time in seconds since Jan 1, 1970
TIMEZONE = 'America/Denver'  # Replace with your desired timezone

def get_ntp_time(host, port):
    """
    Query the NTP server for the current time in UTC.
    """
    try:
        # Create a UDP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # NTP request data (mode 3 - client, version 3)
        data = b'\x1b' + 47 * b'\0'

        # Send the request to the NTP server
        client.sendto(data, (host, port))

        # Receive the response and extract the time
        data, address = client.recvfrom(1024)
        if data:
            t = struct.unpack('!12I', data)[10]
            t -= TIME1970
            return datetime.datetime.utcfromtimestamp(t), t
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None, None
    finally:
        client.close()

def convert_to_timezone(dt, tz_name):
    """
    Convert a datetime object to a specified timezone.
    """
    tz = zoneinfo.ZoneInfo(tz_name)
    return dt.astimezone(tz)

def main():
    # Get NTP time
    utc_time, timestamp = get_ntp_time(NTP_SERVER, NTP_PORT)

    if utc_time:
        # Convert UTC time to the specified timezone
        local_time = convert_to_timezone(utc_time, TIMEZONE)
        print(f"Time from NTP server {NTP_SERVER}: {local_time} (UTC: {utc_time})")
    else:
        print("Failed to retrieve NTP time.")

if __name__ == "__main__":
    main()
