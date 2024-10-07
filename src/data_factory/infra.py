

class ServerInformation():
    '''
    Server Information : server_detais dict structure

    {
    'Environment': 'environment',
    'HostName': 'host_name',
    'Role' : 'role',
    'PlatformType': 'platform_type',
    'SharedOrDedicated: 'shared_or_dedicated',
    'OS': 'os',
    'OSFeatures': 'os_features',
    'CPU': 'cpu',
    'RAM': 'ram',
    'OSDiskGB': 'os_disk_gb',
    'DataDiskCount': 'data_disk_count',
    'SharedDataStore': 'shared_data_store',
    }
    '''
    def __init__(self, server_name: str, server_details: dict):
        self.server_name = server_name
        self.server_details = server_details



class NetworkInformation():
    '''
    Network Information : network_details dict structure

    {
    'Environment': 'environment',
    'HostName': 'host_name',
    'NetworkName': 'network_name',
    'NetworkRange' 'network_range',
    'Subnet': 'subnet',
    'IPAddress': 'ip_address'
    }
    '''
    def __init__(self, network_name: str, network_details: dict):
        self.network_name = network_name
        self.network_details = network_details


class NetworkInterfaces():