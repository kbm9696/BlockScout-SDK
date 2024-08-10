# BlockScout-SDK
Welcome to the BlockScout Python SDK! This library provides a simple interface for interacting with the BlockScout blockchain, making it easy to build blockchain-based applications in Python. The SDK is available as a PIP package for easy installation and usage.

## Installation

You can install the Fraxtal Python SDK using pip:

```bash
pip install BlockScoutSDK
Package Url: https://pypi.org/project/BlockScountSDK/1.0.0/
```
## Access APIS
```bash
from BlockScoutSDK import base
from BlockScoutSDK import blast
from BlockScoutSDK import optimism
from BlockScoutSDK import polygon
from BlockScoutSDK import eth

# Accessing BaseApis from BlockScout
bs_base = base.BaseApi()
bs_base.set_api_key_token('0x12344556')
res = bs_base.get_addresses()

# Accessing BlastApis from BlockScout
bs_blast = blast.BlastApi()
bs_blast.set_api_key_token('0x12345677')
res = bs_blast.get_addresses()

# Accessing EthApis from BlockScout
bs_eth = eth.EthApi()
bs_eth.set_api_key_token('0x123456787')
res = bs_eth.get_addresses()

# Accessing OptimismApis from BlockScout
bs_optimism = optimism.OptimismApi()
bs_optimism.set_api_key_token('0x12345678')
res = bs_optimism.get_addresses()

# Accessing PolygonApis from BlockScout
bs_polygon = polygon.PolygonApi()
bs_polygon.set_api_key_token('0x12345567')
res = bs_polygon.get_addresses()

```
