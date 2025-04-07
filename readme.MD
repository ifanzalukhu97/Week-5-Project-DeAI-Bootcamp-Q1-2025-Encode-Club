# Week 5 Project - AI GPT Bootcamp Q1 2025 - Encode Club

This project is an evolution of the [Week 1 Project](https://github.com/ifanzalukhu97/Week-1-Project-DeAI-Bootcamp-Q1-2025-Encode-Club). In Week 5, we've made significant modifications to enhance the project's decentralization and blockchain integration:

1. Replaced OpenAI APIs with decentralized inference using Together AI for a more decentralized approach to AI implementation
2. Implementing smart contracts to handle recipe storage and management
3. Integration of Web3 capabilities to create a more decentralized and transparent AI service

## Project Result
![Project Result](images/result.png)

## Project Description

This project involves developing a decentralized Chef GPT Script with unique personalities that can:
- Give delicious dish ideas based on ingredients
- Provide recipes for the dishes
- Offer tips or critiques based on the ingredients
- Store recipes on the blockchain using smart contracts

Each script features a distinct AI chef personality, powered by decentralized AI inference and blockchain storage.

## Upcoming Enhancements

We're working on the following enhancements to make our project even more decentralized:

### Decentralized Inference Options
We're replacing the current inference system with fully decentralized alternatives:

1. **OAO (Onchain AI Oracle)**
   - Fully decentralized inference running on the blockchain
   - More expensive but truly decentralized solution
   - Requires SepoliaETH for testing and development
   
2. **Venice AI API**
   - Alternative decentralized inference option
   - Offers free trial with rate limits
   - Potentially more cost-effective for development

### Enhanced Smart Contract Features
We're expanding our smart contract capabilities with:

1. **Recipe Storage Improvements**
   - Enhanced recipe metadata storage
   - Better ownership tracking
   - Recipe versioning capabilities
   
2. **Payment Integration**
   - Wallet-based payment system before using Chef GPT
   - Pay-per-use model for accessing decentralized AI inference
   - Token-based access control

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed Python 3.8 or later
- You have installed pip (Python package installer)
- You have Node.js installed (Note: Currently using v23.10.0, but recommended to use LTS version)
- You have npm installed for smart contract development
- You have set up your Together AI API key (Sign up at https://api.together.ai/signin)
- For upcoming features: SepoliaETH for OAO or Venice AI API access

## Contract Deployment Information
The smart contract has been deployed with the following details:
- **Contract Name**: RecipeStorage
- **Contract Address**: `0x5FbDB2315678afecb367f032d93F642f64180aa3`
- **Network**: Local Hardhat Network (chainId: 31337)
- **Solidity Version**: 0.8.28

## Environment Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/ifanzalukhu97/Week-5-Project-DeAI-Bootcamp-Q1-2025-Encode-Club.git
    cd Week-5-Project-DeAI-Bootcamp-Q1-2025-Encode-Club
    ```

2. **Install Node.js Dependencies**:
    ```sh
    npm install
    ```

3. **Create Environment File**:
    Create a `.env` file in the root directory with the following content:
    ```
    TOGETHER_API_KEY=your_together_api_key
    RECIPE_CONTRACT_ADDRESS=0x5FbDB2315678afecb367f032d93F642f64180aa3
    PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
    ```
    Note: The PRIVATE_KEY provided is the default first account from Hardhat's local node.

4. **Python Virtual Environment Setup**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .\.venv\Scripts\activate
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start Local Blockchain**:
    ```sh
    npx hardhat node
    ```
    This will start a local Ethereum node with predefined accounts and private keys.

2. **Deploy Smart Contract** (in a new terminal):
    ```sh
    npx hardhat run scripts/deploy.js --network localhost
    ```
    The contract should deploy to the address: `0x5FbDB2315678afecb367f032d93F642f64180aa3`

3. **Run the Chef GPT Application**:
    ```sh
    python main.py
    ```

## Features

1. **AI Chef Personalities**:
   - Indian chef specializing in Biryani
   - Italian chef with pasta expertise
   - Brazilian grandma with classic recipes

2. **Recipe Management**:
   - Generate recipes using AI
   - Store recipes on blockchain
   - Retrieve stored recipes
   - Update and delete recipes (by owner)

3. **Blockchain Integration**:
   - Decentralized recipe storage
   - Recipe ownership tracking
   - Transparent recipe history
   - Immutable recipe records

4. **Upcoming Payment System**:
   - Connect your wallet to use the application
   - Pay small fee to access AI inference
   - Transaction-based usage model

## Smart Contract Details

The `RecipeStorage` smart contract (`0x5FbDB2315678afecb367f032d93F642f64180aa3`) provides:
- Recipe creation and storage
- Recipe retrieval by ID
- Recipe updates (owner only)
- Recipe deletion (owner only)
- Chef-specific recipe listing
- Recipe count tracking

## Decentralized Inference Implementation

### Current Implementation
- Together AI for decentralized AI model access
- Uses Llama 3.3 70B model for high-quality recipes
- Structured output parsing for recipe format

### Planned OAO Implementation
- Integration with Onchain AI Oracle
- Blockchain-based inference execution
- Higher decentralization but requires more gas
- Testing on Sepolia testnet before mainnet deployment

### Planned Venice AI Integration
- Alternative to OAO with lower costs
- API-based access to decentralized AI models
- Free tier available for testing and development
- Rate limits apply to free tier usage

## Payment System Implementation (Planned)

We're designing a payment system that will:
1. Require wallet connection before using Chef GPT
2. Charge a small fee for each AI query
3. Use smart contracts for transparent payment handling
4. Provide receipts for all transactions
5. Allow subscription options for frequent users

## Troubleshooting

1. **Node.js Version Warning**:
   - Current setup uses Node.js v23.10.0
   - If you encounter issues, consider downgrading to an LTS version
   - Hardhat is tested with Node.js versions 16.x, 18.x, and 20.x

2. **Contract Deployment Issues**:
   - Ensure Hardhat node is running
   - Verify network configuration in hardhat.config.js
   - Check that the local network (http://127.0.0.1:8545) is accessible

3. **Python Integration Issues**:
   - Verify all environment variables are set correctly
   - Ensure the contract address matches the deployed contract
   - Check that the private key corresponds to a funded account

4. **Decentralized Inference Issues**:
   - For OAO: Ensure sufficient SepoliaETH in wallet
   - For Venice AI: Verify API key and rate limits
   - Check network connection to decentralized services

## How to Contribute

We welcome contributions to our decentralized Chef GPT project:

1. Fork the repository
2. Create a feature branch
3. Implement enhancements or fixes
4. Submit a pull request

Areas we're particularly interested in:
- Decentralized inference optimizations
- Smart contract security improvements
- Payment system implementation
- User interface enhancements

## Contributors
- [ifanzalukhu97](https://github.com/ifanzalukhu97) (Unique ID: S3lFve)
- [joyjsmun](https://github.com/ifanzalukhu97) (Unique ID: OFVwFA)
- [n.vinnikov](https://github.com/n.vinnikov) (Unique ID: VvZfPu)

## License
This project is licensed under the MIT License - see the LICENSE file for details.