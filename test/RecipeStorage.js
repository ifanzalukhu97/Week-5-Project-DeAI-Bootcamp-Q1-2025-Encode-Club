const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("RecipeStorage", function () {
  let RecipeStorage;
  let recipeStorage;
  let owner;
  let addr1;
  let addr2;

  // Sample recipe data
  const sampleRecipe = {
    name: "Spaghetti Carbonara",
    ingredients: "Pasta, Eggs, Pecorino Romano, Pancetta, Black Pepper",
    instructions: "1. Cook pasta 2. Mix eggs and cheese 3. Combine and add pancetta"
  };

  beforeEach(async function () {
    // Get contract factory and signers
    RecipeStorage = await ethers.getContractFactory("RecipeStorage");
    [owner, addr1, addr2] = await ethers.getSigners();

    // Deploy contract
    recipeStorage = await RecipeStorage.deploy();
  });

  describe("Recipe Creation", function () {
    it("Should create a new recipe", async function () {
      await recipeStorage.createRecipe(
        sampleRecipe.name,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      );

      const recipe = await recipeStorage.getRecipe(0);
      expect(recipe.name).to.equal(sampleRecipe.name);
      expect(recipe.ingredients).to.equal(sampleRecipe.ingredients);
      expect(recipe.instructions).to.equal(sampleRecipe.instructions);
      expect(recipe.chef).to.equal(await owner.getAddress());
    });

    it("Should emit RecipeCreated event", async function () {
      await expect(recipeStorage.createRecipe(
        sampleRecipe.name,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      ))
        .to.emit(recipeStorage, "RecipeCreated")
        .withArgs(0, sampleRecipe.name, await owner.getAddress());
    });

    it("Should increment recipe count", async function () {
      await recipeStorage.createRecipe(
        sampleRecipe.name,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      );

      expect(await recipeStorage.getRecipeCount()).to.equal(1);
    });
  });

  describe("Recipe Retrieval", function () {
    beforeEach(async function () {
      await recipeStorage.createRecipe(
        sampleRecipe.name,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      );
    });

    it("Should retrieve existing recipe", async function () {
      const recipe = await recipeStorage.getRecipe(0);
      expect(recipe.name).to.equal(sampleRecipe.name);
    });

    it("Should fail to retrieve non-existent recipe", async function () {
      await expect(recipeStorage.getRecipe(99))
        .to.be.revertedWith("Recipe does not exist");
    });

    it("Should get chef's recipes", async function () {
      const recipes = await recipeStorage.getChefRecipes();
      expect(recipes.length).to.equal(1);
      expect(recipes[0]).to.equal(0);
    });
  });

  describe("Recipe Updates", function () {
    beforeEach(async function () {
      await recipeStorage.createRecipe(
        sampleRecipe.name,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      );
    });

    it("Should update recipe by owner", async function () {
      const newName = "Updated Carbonara";
      await recipeStorage.updateRecipe(
        0,
        newName,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      );

      const recipe = await recipeStorage.getRecipe(0);
      expect(recipe.name).to.equal(newName);
    });

    it("Should fail when non-owner tries to update", async function () {
      await expect(recipeStorage.connect(addr1).updateRecipe(
        0,
        "Hacked Recipe",
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      )).to.be.revertedWith("Not the recipe owner");
    });

    it("Should emit RecipeUpdated event", async function () {
      const newName = "Updated Carbonara";
      await expect(recipeStorage.updateRecipe(
        0,
        newName,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      ))
        .to.emit(recipeStorage, "RecipeUpdated")
        .withArgs(0, newName, await owner.getAddress());
    });
  });

  describe("Recipe Deletion", function () {
    beforeEach(async function () {
      await recipeStorage.createRecipe(
        sampleRecipe.name,
        sampleRecipe.ingredients,
        sampleRecipe.instructions
      );
    });

    it("Should delete recipe by owner", async function () {
      await recipeStorage.deleteRecipe(0);
      await expect(recipeStorage.getRecipe(0))
        .to.be.revertedWith("Recipe does not exist");
    });

    it("Should fail when non-owner tries to delete", async function () {
      await expect(recipeStorage.connect(addr1).deleteRecipe(0))
        .to.be.revertedWith("Not the recipe owner");
    });

    it("Should emit RecipeDeleted event", async function () {
      await expect(recipeStorage.deleteRecipe(0))
        .to.emit(recipeStorage, "RecipeDeleted")
        .withArgs(0, await owner.getAddress());
    });
  });
}); 