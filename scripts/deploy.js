const hre = require("hardhat");

async function main() {
  console.log("Deploying RecipeStorage contract...");

  // Deploy the contract
  const RecipeStorage = await hre.ethers.getContractFactory("RecipeStorage");
  const recipeStorage = await RecipeStorage.deploy();

  await recipeStorage.waitForDeployment();
  const address = await recipeStorage.getAddress();

  console.log("RecipeStorage deployed to:", address);
}

// Handle errors
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
}); 