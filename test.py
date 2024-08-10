import sys

import base
import blast
import optimism
import polygon
import eth


# Accessing BaseApis from BlockScout
bs_base = base.BaseApi()
bs_base.set_api_key_token('0x12344556')
a = bs_base.get_addresses()
print('base',a)

# Accessing BlastApis from BlockScout
bs_blast = blast.BlastApi()
bs_blast.set_api_key_token('f8871921-9d54-4916-bb23-c56d8787b5a4')
a = bs_blast.get_addresses()
print('blast',a)

# Accessing EthApis from BlockScout
bs_eth = eth.EthApi()
bs_eth.set_api_key_token('f8871921-9d54-4916-bb23-c56d8787b5a4')
address = bs_eth.get_addresses()
print('eth',address)

# Accessing OptimismApis from BlockScout
bs_optimism = optimism.OptimismApi()
bs_optimism.set_api_key_token('f8871921-9d54-4916-bb23-c56d8787b5a4')
a = bs_optimism.get_addresses()
print('optimism',a)

# Accessing PolygonApis from BlockScout
bs_polygon = polygon.PolygonApi()
bs_polygon.set_api_key_token('f8871921-9d54-4916-bb23-c56d8787b5a4')
a = bs_polygon.get_addresses()
print('polygon',a)

