from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    OPENSEA_FORMAT,
    get_contract,
)
from brownie import AdvancedCollectible, network, config

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config[network.show_active()]["keyhast"],
        config[network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New Token has been created")


def main():
    deploy_and_create()
