#este scrpit usa nmap para escanear tu red para visualizar dispositivos y visualizar su informacion.
import nmap

# Inicializar el escáner
nm = nmap.PortScanner()

# Escanear el rango de direcciones IP para el puerto 22 (SSH)
nm.scan(hosts='192.168.1.0/24', arguments='-p 22')

# Mostrar resultados
for host in nm.all_hosts():
    print('Host: %s (%s)' % (host, nm[host].hostname() if 'hostname' in nm[host] else 'Desconocido'))
    print('Estado: %s' % nm[host].state())
    if nm[host].state() == 'up':
        for proto in nm[host].all_protocols():
            print('Protocolo: %s' % proto)
            ports = nm[host][proto].keys()
            for port in ports:
                print('Puerto: %s\tEstado: %s' % (port, nm[host][proto][port]['state']))


