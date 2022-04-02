from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import AdvancedConllectible, network, config

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedConllectible.deploy(
        config[network.show_active()]["vrf_coordinator"],
        config[network.show_active()]["link_token"],
        config[network.show_active()]["keyhast"],
        config[network.show_active()]["fee"],
        {"from": account},
    )


def main():
    deploy_and_create()
