from web3 import Web3
from eth_account import Account
import json
import os
from dotenv import load_dotenv
import binascii
import traceback

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
        if not self.contract_address:
            raise ValueError("RECIPE_CONTRACT_ADDRESS not found in environment variables")
        
        # Convert address to checksum format
        self.contract_address = Web3.to_checksum_address(self.contract_address)
        
        # Initialize contract
        self.contract = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
        
        # Set up account from private key
        self.private_key = os.getenv('PRIVATE_KEY')
        if not self.private_key:
            raise ValueError("PRIVATE_KEY not found in environment variables")
        if not self.private_key.startswith('0x'):
            self.private_key = '0x' + self.private_key
        
        # Create account from private key
        self.account = self.w3.eth.account.from_key(self.private_key)
        self.address = self.account.address
        print(f"Connected with account: {self.address}")

    def save_recipe(self, name, ingredients, instructions):
        """Save a recipe to the blockchain"""
        try:
            # Check connection
            if not self.w3.is_connected():
                raise ConnectionError("Not connected to Ethereum network")
            
            print(f"Preparing to save recipe: {name}")
            
            # Get latest nonce
            nonce = self.w3.eth.get_transaction_count(self.address)
            print(f"Current nonce: {nonce}")
            
            # Build the transaction
            create_recipe_tx = self.contract.functions.createRecipe(
                name,
                ingredients,
                instructions
            ).build_transaction({
                'chainId': 31337,
                'from': self.address,
                'gas': 2000000,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': nonce,
            })
            
            print("Transaction built, signing...")
            
            # Sign transaction
            signed_tx = self.account.sign_transaction(create_recipe_tx)
            
            print("Transaction signed, sending...")
            
            # Send raw transaction
            # In Web3.py 7.x, we need to access .raw_transaction (note the underscore)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            
            print(f"Transaction sent with hash: {tx_hash.hex()}")
            
            # Wait for transaction receipt
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            # Access block_number as a dictionary key instead of an attribute
            print(f"Transaction confirmed in block {receipt['blockNumber']}")
            
            return receipt
        
        except Exception as e:
            print(f"Error saving recipe: {str(e)}")
            traceback.print_exc()
            raise Exception(f"Failed to save recipe to blockchain: {str(e)}")

    def get_recipe(self, recipe_id):
        """Retrieve a recipe from the blockchain"""
        if not self.w3.is_connected():
            raise ConnectionError("Not connected to Ethereum network")
            
        try:
            return self.contract.functions.getRecipe(recipe_id).call()
        except Exception as e:
            print(f"Error fetching recipe {recipe_id}: {str(e)}")
            raise

    def get_chef_recipes(self):
        """Get all recipes created by the current chef"""
        if not self.w3.is_connected():
            raise ConnectionError("Not connected to Ethereum network")
            
        try:
            return self.contract.functions.getChefRecipes().call({
                'from': self.address
            })
        except Exception as e:
            print(f"Error fetching chef recipes: {str(e)}")
            raise 