 #Verificação de Dispositivos na Rede Local
#Este código usa a biblioteca scapy para realizar uma varredura na rede local em busca de dispositivos.

python
Copy code
from scapy.all import ARP, Ether, srp

def verifica_dispositivos_na_rede(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    resultado = srp(arp_request_broadcast, timeout=3, verbose=False)[0]
    dispositivos = []
    for sent, received in resultado:
        dispositivos.append({'ip': received.psrc, 'mac': received.hwsrc})
    return dispositivos

if __name__ == "__main__":
    rede = "192.168.0.1/24"  # Substitua pela sua rede
    dispositivos_encontrados = verifica_dispositivos_na_rede(rede)
    print("Dispositivos na rede:")
    for dispositivo in dispositivos_encontrados:
        print(f"IP: {dispositivo['ip']}, MAC: {dispositivo['mac']}")