from meraki_sdk.meraki_sdk_client import MerakiSdkClient

API_KEY = '15da0c6ffff295f16267f88f98694cf29a86ed87'

MERAKI = MerakiSdkClient(API_KEY)


ORGS = MERAKI.organizations.get_organizations()



PARAMS = {}
PARAMS['organization_id'] = ORGS[0]['id']

NETS = MERAKI.networks.get_organization_networks(PARAMS)



DEVICES = MERAKI.devices.get_network_devices(NETS[2]['id'])

for DEV in DEVICES :
    print('Device Model: {0:9s},Serial: {1:14s}, MAC: {2:17},Firmware: {3:12s}'\
          .format(DEV['model'],DEV['serial'],DEV['mac'],DEV['firmware']))