from algosdk.kmd import KMDClient
from algosdk.v2client import algod, indexer


kmd_token = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
kmd_address = 'http://localhost:4002'

algod_token = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
algod_address = 'http://localhost:4001'

indexer_token='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
indexer_address='http://localhost:8980'

# Connect to KMD
def get_kmd_client():
 return KMDClient(kmd_token,kmd_address)

# Connect to Algorand
def get_algod_client():
    return algod.AlgodClient(algod_token, algod_address)

def get_indexer_client():
    return indexer.IndexerClient(indexer_token, indexer_address)

