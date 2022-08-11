from clients import *
from kmd import *
from algosdk import account

kmdc = get_kmd_client()
wallet_name = input('wallet name:')
wallet_passwd = input('wallet passwd:')
walletid = kmdc.create_wallet(wallet_name,wallet_passwd)['id']
print('walletid of new wallet is',walletid)

# get handle for just created wallet
wallethandle = kmdc.init_wallet_handle(walletid,wallet_passwd)
print('listing keys..')
keys = kmdc.list_keys(wallethandle)

print('generating new account..')
# generate account
pk1, add1 = account.generate_account()
print('new account',add1)
print('new pk',pk1)
kmdc.import_key(wallethandle,pk1)
print('listing keys..')
keys = kmdc.list_keys(wallethandle)
print(keys)