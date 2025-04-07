from web3 import Web3
from eth_account import Account
import json
import os
from dotenv import load_dotenv

load_dotenv()

class BlockchainRecipeStorage:
    def __init__(self):
        # Connect to local hardhat node
        self.w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        
        # Load contract ABI and address
        with open('artifacts/contracts/RecipeStorage.sol/RecipeStorage.json') as f:
            contract_json = json.load(f)
        self.contract_abi = contract_json['abi']
        
        # Contract address will be set after deployment
        self.contract_address = os.getenv('RECIPE_CONTRACT_ADDRESS')
        
        # Initialize contract
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
        
        # Set up account
        private_key = os.getenv('PRIVATE_KEY')
        self.account = Account.from_key(private_key)

    def save_recipe(self, name, ingredients, instructions):
        """Save a recipe to the blockchain"""
        # Prepare transaction
        transaction = self.contract.functions.createRecipe(
            name,
            ingredients,
            instructions
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        # Sign and send transaction
        signed_txn = self.w3.eth.account.sign_transaction(
            transaction, 
            self.account.key
        )
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        # Wait for transaction receipt
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt

    def get_recipe(self, recipe_id):
        """Retrieve a recipe from the blockchain"""
        return self.contract.functions.getRecipe(recipe_id).call()

    def get_chef_recipes(self):
        """Get all recipes created by the current chef"""
        return self.contract.functions.getChefRecipes().call({'from': self.account.address}) 