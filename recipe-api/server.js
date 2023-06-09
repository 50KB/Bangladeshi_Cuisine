const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;
const { connect } = require('./db');

app.use(cors());

app.get('/recipes', async(req, res) => {
    const db = await connect();
    const collection = db.collection('Recipes');
    const recipe = await collection.findOne({ name: req.params.name });
    if (!recipe) {
        res.status(404).send('Recipe not found');
        return;
    }
    res.send(recipe);
});

app.get('/recipe/name/:name', async(req, res) => {
    const db = await connect();
    const collection = db.collection('Recipes');
    const recipe = await collection.findOne({ name: req.params.name });
    if (!recipe) {
        res.status(404).send('Recipe not found');
        return;
    }
    res.send(recipe);
});

app.get('/recipe/serving/:serving', async(req, res) => {
    const servingSize = req.params.serving;

    const db = await connect();
    const collection = db.collection('Recipes');
    const recipes = await collection.find({ serving: servingSize }).toArray();

    if (recipes.length === 0) {
        res.status(404).send('No recipes found for the specified serving size');
        return;
    }

    res.send(recipes);
});

app.get('/recipe/cooktime/:time', async(req, res) => {
    const cookTime = parseInt(req.params.time);

    const db = await connect();
    const collection = db.collection('Recipes');
    const recipes = await collection.find({ time: cookTime }).toArray();

    if (recipes.length === 0) {
        res.status(404).send('No recipes found for the specified cook time');
        return;
    }

    res.send(recipes);
});

app.get('/recipes', async(req, res) => {
    const db = await connect();
    const collection = db.collection('Recipes');
    const recipes = await collection.find().toArray();
    if (recipes.length === 0) {
        res.status(404).send('No recipes found');
        return;
    }
    const recipeNames = recipes.map((recipe) => recipe.name);
    res.send(recipeNames);
});


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});