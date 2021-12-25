# from scripts.helpful_scripts import get_account
from brownie import network, config, accounts
from brownie import FundMe


def get_account():
    print(network.show_active())
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print(f"get_account() === {get_account()}")
    account = get_account()
    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e", {"from": account}
    )
    print(f"fund_me.address === {fund_me.address}")
    print(f"len(FundMe) === {len(FundMe)}")
    print(f"FundMe[-1] === {FundMe[-1]}")


#! > brownie run ddd.py
#! > brownie run ddd.py --network rinkeby

# * > brownie run ddd.py
# ? > brownie run ddd.py
# todo > brownie run ddd.py
# @ > brownie run ddd.py
