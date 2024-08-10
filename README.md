
# BlockScout Python SDK

Welcome to the BlockScout Python SDK! This library provides a simple and intuitive interface for interacting with the BlockScout blockchain explorer, making it easier than ever to build blockchain-based applications in Python. Whether you're developing analytics dashboards, creating decentralized applications, or exploring blockchain data, this SDK streamlines your workflow and boosts your productivity.

## Why Use BlockScout SDK?

The BlockScout SDK abstracts the complexity of interacting with multiple blockchains, allowing developers to focus on building their applications. By providing a unified interface for interacting with various chains like Optimism, Ethereum, Polygon, Blast, and Base, the SDK simplifies the process of retrieving blockchain data, making it invaluable for developers who need to build powerful dashboards and analytics tools.

With the growing number of blockchain networks, developers face the challenge of managing different APIs and data structures. The BlockScout SDK solves this problem by offering a consistent API across supported chains, enabling rapid development and integration of blockchain data into your projects. Over time, the SDK will expand to support additional chains, ensuring that it remains a versatile tool for your blockchain development needs.

## Installation

You can install the BlockScout Python SDK using pip:

```bash
pip install BlockScoutSDK
```

[Package URL](https://pypi.org/project/BlockScoutSDK/1.0.0/)

## Getting Started

The SDK provides modules for interacting with different blockchains supported by BlockScout. Here's a quick example of how to use the SDK:

```python
from BlockScoutSDK import base
from BlockScoutSDK import blast
from BlockScoutSDK import optimism
from BlockScoutSDK import polygon
from BlockScoutSDK import eth

# Accessing Base APIs from BlockScout
bs_base = base.BaseApi()
bs_base.set_api_key_token('0x12344556')
res = bs_base.get_addresses()

# Accessing Blast APIs from BlockScout
bs_blast = blast.BlastApi()
bs_blast.set_api_key_token('0x12345677')
res = bs_blast.get_addresses()

# Accessing Ethereum APIs from BlockScout
bs_eth = eth.EthApi()
bs_eth.set_api_key_token('0x123456787')
res = bs_eth.get_addresses()

# Accessing Optimism APIs from BlockScout
bs_optimism = optimism.OptimismApi()
bs_optimism.set_api_key_token('0x12345678')
res = bs_optimism.get_addresses()

# Accessing Polygon APIs from BlockScout
bs_polygon = polygon.PolygonApi()
bs_polygon.set_api_key_token('0x12345567')
res = bs_polygon.get_addresses()
```

## Supported Chains

- **Optimism**
- **Ethereum**
- **Polygon**
- **Blast**
- **Base**

Stay tuned for future updates as we add support for more chains, expanding the capabilities of the BlockScout SDK!

## Contributing

We welcome contributions from the community! If you'd like to contribute, please fork the repository and create a pull request. If you encounter any issues or have suggestions for improvements, feel free to open an issue on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For more information, questions, or support, feel free to reach out through the GitHub repository.
