from collector import Collector
from flask import Flask, jsonify
import psutil as ps


app = Flask(__name__)       # init flask application
collector_object = None     # Collector Object  

def get_ip4_by_iface(iface:str) -> str:
    """returns ipv4 address of a given interface

    Args:
        iface (str): interface name

    Returns:
        str: IPv4 address or None 
    """
    try:
        for addr in ps.net_if_addrs()[iface]:
            if str(getattr(addr,'family')).split('.')[1] == 'AF_INET':
                ipv4_addr = getattr(addr,'address')
    except Exception as e:
        ipv4_addr = None
    finally:
        return ipv4_addr


@app.route('/get_utils', methods=['GET'])
def get_utils():
    measurements = collector_object.collect()
    return jsonify(measurements)


if __name__ == '__main__':
    # create a collector object using a given system ip 
    try_counter = 3 # break after 3 trials of wrong interface

    while try_counter: 
        iface_name = input(f'Enter interface name to specify system IP [attempt: {try_counter}/3]: ')
        if get_ip4_by_iface(iface=iface_name):   # if valid interface 
            collector_object = Collector(iface=iface_name) # create a collection object 
            break
        else:
            print('Error: Invalid interface name or interface does not have a valid IPv4 address assigned !')
            try_counter-=1
    
    # continute if iface name has an IP 
    if collector_object:  # if not None 
        app.run(port=5001, host='0.0.0.0')


        