from typing import Set
from pyteal import *


# Based on this video - https://www.youtube.com/watch?v=XKOEYTMKuFc


# Stores a variable called count that is incremented on every call of the program
program = Seq (
    App.globalPut(Bytes("count"),App.globalGet(Bytes("count")) + Int(1)),
    Approve()
)

i = ScratchVar(TealType.uint64)
on_create = Seq (
    For(i.store(Int(0)), i.load()<Int(16),i.store(i.load()+Int(1)))
    .Do(
        App.globalPut(Concat(Bytes("index"),Itob(i.load())),Int(1))
    ),
    Approve()

)

# Payment from escrow account to self
escrow_payment = Seq(
    InnerTxnBuilder.Begin(),
    InnerTxnBuilder.SetFields(
        {
            TxnField.type_enum: TxnType.Payment,
            TxnField.receiver: Txn.sender(),
            TxnField.amount: Int(1_000_000)

        }
    ),
    InnerTxnBuilder.Submit(),
    Approve()
)

appAddr = Global.current_application_address()

# Coin
chainhaus_coin = Seq (
    InnerTxnBuilder.Begin(),
    InnerTxnBuilder.SetFields (
        {
            TxnField.type_enum: TxnType.AssetConfig,
            TxnField.config_asset_name: Bytes ('Chainhaus Coin'),
            TxnField.config_asset_unit_name: Bytes("CH"),
            TxnField.config_asset_url: Bytes("https://chainhaus.com"),
            TxnField.config_asset_decimals: Int(6),
            TxnField.config_asset_total: Int(800_000_000),
            TxnField.config_asset_manager: appAddr
        }
    ),
    InnerTxnBuilder.Submit(),
    App.globalPut(Bytes("Chainhaus Coin ID"),InnerTxn.created_asset_id()),
    Approve()
)


teal_source = compileTeal(chainhaus_coin,mode=Mode.Application,version=5)
print(teal_source)
