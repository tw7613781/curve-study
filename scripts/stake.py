# run the script in mainnet-fork only
# brownie run scripts/stake.py --network mainnet-fork

from brownie import Contract, accounts
from brownie_tokens import MintableForkToken

def main():
    dai_addr = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
    usdc_addr = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    registry_addr = "0x7D86446dDb609eD0F5f8684AcF30380a356b2B4c"

    amount = 100_000 * 10 ** 18
    dai = MintableForkToken(dai_addr)
    dai._mint_for_testing(accounts[0], amount)

    ## 没有interface的情况下，使用Contract
    registry = Contract(registry_addr)
    pool_addr = registry.find_pool_for_coins(dai_addr, usdc_addr)
    pool = Contract(pool_addr)

    dai.approve(pool_addr, amount, {'from': accounts[0]})
    pool.add_liquidity([amount, 0, 0], 0, {'from': accounts[0]})

