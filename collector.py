import psutil as ps
import datetime as dt


class Collector:
    def __init__(self, iface:str) -> None:
        """collector class: Collects local KPIs

        Args:
            iface (str): name of the interface by whose IP address the system would be identified
        """
        try:
            for addr in ps.net_if_addrs()[iface]:
                if str(getattr(addr,'family')).split('.')[1] == 'AF_INET':
                    self.system_ip = getattr(addr,'address')
        except Exception as e:
            self.system_ip = None    
    
    def collect(self) -> dict:
        """Collects KPI when called

        Returns:
            dict: collected sample
        """
        
        self.sample = {
                        '_sys_timestamp' : str(dt.datetime.now()),
                        '_sys_ip' : self.system_ip,
                        'kpi':{}
                    }

        ## CPU KPI
        self.sample['kpi']['cpu_pct'] = ps.cpu_percent(interval=None)     # non blocking cpu % usage 
        self.sample['kpi']['cpu_count'] = ps.cpu_count(logical=False)     # number of physical cores     
        self.sample['kpi']['cpu_freq'] = getattr(ps.cpu_freq(percpu=False),'current') # average frequency
        self.sample['kpi']['cpu_load'] = ps.getloadavg()[0]               # average frequency for last 1 minuete 
                

        ## Mem KPI
        virt_mem_state = ps.virtual_memory()    # get virtual memory state 
        swap_mem_state = ps.swap_memory()       # get swap memory state 

        self.sample['kpi']['virt_mem_pct'] = getattr(virt_mem_state,'percent')   # memeory usage % 
        self.sample['kpi']['virt_mem_total'] = getattr(virt_mem_state,'total')//(2**30)   # memeory total in GB
        self.sample['kpi']['swap_mem_pct'] = getattr(swap_mem_state,'percent')   # memeory usage % 
        self.sample['kpi']['swap_mem_total'] = getattr(swap_mem_state,'total')//(2**30)   # memeory total in GB

        ## Disk KPI
        disk_state = ps.disk_usage('/')

        self.sample['kpi']['disk_total'] = getattr(disk_state, 'total')//(2**30)  # disk total in GB
        self.sample['kpi']['disk_pct'] = getattr(disk_state, 'percent')           # disk usage %
        
        ## NIC KPI
        nic_state = ps.net_io_counters(pernic=False, nowrap=True)    # get the NIC state 

        self.sample['kpi']['nic_bytes_sent']=getattr(nic_state, 'bytes_sent')
        self.sample['kpi']['nic_bytes_recv']=getattr(nic_state, 'bytes_recv')
        self.sample['kpi']['nic_packets_sent']=getattr(nic_state, 'packets_sent')
        self.sample['kpi']['nic_packets_recv']=getattr(nic_state, 'packets_recv')
        self.sample['kpi']['nic_errin']=getattr(nic_state, 'errin')
        self.sample['kpi']['nic_errout']=getattr(nic_state, 'errout')
        self.sample['kpi']['nic_dropin']=getattr(nic_state, 'dropin')
        self.sample['kpi']['nic_dropout']=getattr(nic_state, 'dropout')
        
        return self.sample