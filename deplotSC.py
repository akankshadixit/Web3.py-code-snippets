import json
from web3 import Web3 

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress("0x31de18a483eC932685EE00792e763768233EA5EA")

contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('Hello its a new message!!').transact()

web3.eth.waitForTransactionReceipt(tx_hash)
print('Updated Greeting: {}'.format(
    contract.functions.greet().call()
))

