from scapy.all import *
import logging

# Thiết lập logging
logging.basicConfig(filename='ids.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Hàm để phát hiện các gói tin đáng ngờ
def detect_packet(packet):
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        ip_layer = packet.getlayer(IP)
        
        # Phát hiện SYN Flooding (nhiều gói SYN được gửi đến)
        if tcp_layer.flags == 'S':
            logging.info(f"SYN packet detected from {ip_layer.src} to {ip_layer.dst}")
        
        # Phát hiện các gói có các cổng phổ biến của các dịch vụ
        if tcp_layer.dport in [21, 22, 23, 80, 443]:  # FTP, SSH, Telnet, HTTP, HTTPS
            logging.info(f"Packet to common port {tcp_layer.dport} detected from {ip_layer.src} to {ip_layer.dst}")
    
    elif packet.haslayer(UDP):
        udp_layer = packet.getlayer(UDP)
        ip_layer = packet.getlayer(IP)
        
        # Phát hiện các gói UDP đến các cổng phổ biến của các dịch vụ
        if udp_layer.dport in [53, 69, 161]:  # DNS, TFTP, SNMP
            logging.info(f"UDP packet to common port {udp_layer.dport} detected from {ip_layer.src} to {ip_layer.dst}")

# Bắt gói tin và gọi hàm detect_packet cho mỗi gói tin
def start_sniffing(interface):
    sniff(iface=interface, prn=detect_packet, store=False)

# Chạy chương trình
if __name__ == "__main__":
    interface = "Wi-Fi"  # Đổi interface này thành interface mạng của bạn
    print(f"Starting IDS on interface {interface}")
    start_sniffing(interface)
