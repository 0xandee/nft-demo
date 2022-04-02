from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleConllectible

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def main():
    account = get_account()
    simple_collectible = SimpleConllectible.deploy({"from": account})
    tx = simple_collectible.createConllectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
    return simple_collectible
