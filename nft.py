from algosdk.v2client import algod, indexer
from algosdk import account, mnemonic, kmd
from algosdk.future.transaction import AssetCreateTxn
import json, base64
from algosdk.future.transaction import AssetCreateTxn
from algosdk.atomic_transaction_composer import *
from algosdk.future.transaction import *
from algosdk.abi import *

from clients import *
from clients import get_kmd_client
from algosdk.future.transaction import *

kmdc = get_kmd_client()

#obtain sender
wallets = kmdc.list_wallets()
walletid = wallets[0].get('id')
wallethandle = kmdc.init_wallet_handle(walletid,'')
accounts = kmdc.list_keys(wallethandle)
sender_acc = accounts[0]
print(accounts[0])

# sk,pk = account.generate_account()
# print(pk)
# print(sk)
pk = sender_acc
sk = kmdc.export_key(wallethandle,'',sender_acc).encode()

#acc = 'KZEAJKQIADHBKGI6QWDNZJAEW2NDBJ7E7YHU5RQRQJEIHS5PXYNNWGAW3Y'
algod_address = 'http://localhost:4001'
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)
params = algod_client.suggested_params()
print('params',params)
#account_info = algod_client.account_info(acc)
txn = AssetCreateTxn(
    sender=pk,
    sp=params,
    total=1,
    default_frozen=False,
    unit_name="LATINUM",
    asset_name="latinum",
    manager=pk,
    reserve=pk,
    freeze=pk,
    clawback=pk,
    url="https://path/to/my/asset/details", 
    decimals=0)

stxn = txn.sign(sk)
txid =algod_client.send_transaction(stxn)
confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
ptx = algod_client.pending_transaction_info(txid)
asset_id = ptx["asset-index"]
print(ptx)
print(asset_id)
print("TXID: ", txid)
print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round'])) 

