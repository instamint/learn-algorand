from algosdk import account, mnemonic, kmd
from algosdk.kmd import KMDClient
from clients import *
from clients import get_kmd_client

kmdc = get_kmd_client()

def list_wallets():
    wallets = kmdc.list_wallets()
    for w in wallets:
        print(w)
    return wallets

def list_keys(wallethandle):
    keys = kmdc.list_keys(wallethandle)
    for k in keys:
        print(k)
    return keys

# wallets = list_wallets()
# walletid = wallets[0].get('id')
# print('walletid',walletid)
# wallethandle = kmdc.init_wallet_handle(walletid,'')
# print('wallethandle',wallethandle)
# keys = list_keys(wallethandle)
# pk = kmdc.export_key(wallethandle,'',keys[0])
# print('private key for',keys[0],'is',pk)

# print(kmdc.list_wallets())
# # pk = kmdc.export_key('','','W6FSQDZBIGHIXFAKJLJWVCJIHCKFSF3JUNPSKEBVPDCMAIMVKPVSI3NUCY')
# # print(pk)
# pk = mnemonic.to_private_key('milk provide salmon angle churn release wonder enact wish devote bless wheat float glass sign stand maid spy any damp divide bonus angle able claim')
# print(pk)