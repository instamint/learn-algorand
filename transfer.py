from algosdk.future import transaction
from algosdk import constants
from clients import *


##### transfer from sender account[0] to receiver account[1]
kmdc = get_kmd_client()
algodc = get_algod_client()

# obtain sender
wallets = kmdc.list_wallets()
walletid = wallets[0].get('id')
wallethandle = kmdc.init_wallet_handle(walletid,'')
accounts = kmdc.list_keys(wallethandle)
sender_acc = accounts[0]

# get senders private key
private_key = kmdc.export_key(wallethandle,'',sender_acc).encode()

# obtain receiver
receiver_acc = accounts[1]


#account_info = algod_client.account_info(sender_acc)

params = algodc.suggested_params()
print(params.__dict__)
# comment out the next two (2) lines to use suggested fees
params.flat_fee = True
params.fee = constants.MIN_TXN_FEE 
note = "Hello World".encode()
amount = 10000000000
unsigned_txn = transaction.PaymentTxn(sender_acc, params, receiver_acc, amount, None, note)
signed_tx = unsigned_txn.sign(private_key)
txid = algodc.send_transaction(signed_tx)
print('txid',txid)