// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract RecipeStorage {
    // Structure for Recipe
    struct Recipe {
        string name;
        string ingredients;
        string instructions;
        address chef;
        uint256 timestamp;
        bool exists;
    }

    // State variables
    uint256 public recipeCount;
    mapping(uint256 => Recipe) public recipes;
    mapping(address => uint256[]) public chefRecipes;

    // Events
    event RecipeCreated(uint256 indexed recipeId, string name, address indexed chef);
    event RecipeUpdated(uint256 indexed recipeId, string name, address indexed chef);
    event RecipeDeleted(uint256 indexed recipeId, address indexed chef);

    // Modifiers
    modifier onlyRecipeOwner(uint256 _recipeId) {
        require(recipes[_recipeId].chef == msg.sender, "Not the recipe owner");
        _;
    }

    modifier recipeExists(uint256 _recipeId) {
        require(recipes[_recipeId].exists, "Recipe does not exist");
        _;
    }

    // Functions
    function createRecipe(
        string memory _name,
        string memory _ingredients,
        string memory _instructions
    ) public returns (uint256) {
        uint256 recipeId = recipeCount;
        
        recipes[recipeId] = Recipe({
            name: _name,
            ingredients: _ingredients,
            instructions: _instructions,
            chef: msg.sender,
            timestamp: block.timestamp,
            exists: true
        });

        chefRecipes[msg.sender].push(recipeId);
        recipeCount++;

        emit RecipeCreated(recipeId, _name, msg.sender);
        return recipeId;
    }

    function getRecipe(uint256 _recipeId) 
        public 
        view 
        recipeExists(_recipeId)
        returns (
            string memory name,
            string memory ingredients,
            string memory instructions,
            address chef,
            uint256 timestamp
        ) 
    {
        Recipe storage recipe = recipes[_recipeId];
        return (
            recipe.name,
            recipe.ingredients,
            recipe.instructions,
            recipe.chef,
            recipe.timestamp
        );
    }

    function updateRecipe(
        uint256 _recipeId,
        string memory _name,
        string memory _ingredients,
        string memory _instructions
    ) 
        public 
        recipeExists(_recipeId)
        onlyRecipeOwner(_recipeId)
    {
        Recipe storage recipe = recipes[_recipeId];
        recipe.name = _name;
        recipe.ingredients = _ingredients;
        recipe.instructions = _instructions;
        recipe.timestamp = block.timestamp;

        emit RecipeUpdated(_recipeId, _name, msg.sender);
    }

    function deleteRecipe(uint256 _recipeId) 
        public 
        recipeExists(_recipeId)
        onlyRecipeOwner(_recipeId)
    {
        delete recipes[_recipeId];
        emit RecipeDeleted(_recipeId, msg.sender);
    }

    function getChefRecipes() public view returns (uint256[] memory) {
        return chefRecipes[msg.sender];
    }

    function getRecipeCount() public view returns (uint256) {
        return recipeCount;
    }
} 