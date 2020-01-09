import json
from web3 import Web3 

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0xA4ede8B380B041AD935B80f1585b8349FFd0b34A'
account_2 = '0xd1AAFC6B9f1Ea4a76631E7028E18abB18Bb454f6'

private_key = 'f5e5348d8ec91c2a61dc372dcf1db8d595a91f8e242493ce386bae9480b43dfc'

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_txn = web3.eth.account.signTransaction(tx,private_key)

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(web3.toHex(tx_hash))