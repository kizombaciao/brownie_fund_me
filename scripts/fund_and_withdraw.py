from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    print(f"fund_me === {fund_me}")
    account = get_account()
    print(f"account === {account}")
    # ttt = fund_me.getPrice()
    # print(ttt)
    entrance_fee = fund_me.getEntranceFee()
    print(f"entrance_fee === {entrance_fee}")
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    # withdraw()
