import React, { useState, useEffect } from 'react';
import './App.css';
import backgroundImage from './image/background1.jpg';

function App() {
  const [recipes, setRecipes] = useState([]);
  const [ingredientName, setIngredientName] = useState('');
  const [servnum, setServnum] = useState('');
  const [ct, setCt] = useState('');
  const [searchPerformed, setSearchPerformed] = useState(false);
  const [searchResult, setSearchResult] = useState(true);
  

  const handleIngredientSearch = () => {
    fetch(`http://localhost:5000/recipe/name/${ingredientName}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setRecipes(data);
        setSearchPerformed(true);
        setSearchResult(data.length > 0);
      })
      .catch((error) => {
        console.error('Error retrieving recipes:', error);
      });
  };

  const handleDietSearch = () => {
    fetch(`http://localhost:5000/recipe/serving/${servnum}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setRecipes(data);
        setSearchPerformed(true);
        setSearchResult(data.length > 0);
      })
      .catch((error) => {
        console.error('Error retrieving recipes:', error);
      });
  };

  const handleCtSearch = () => {
    fetch(`http://localhost:5000/recipe/cooktime/${ct}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setRecipes(data);
        setSearchPerformed(true);
        setSearchResult(data.length > 0);
      })
      .catch((error) => {
        console.error('Error retrieving recipes:', error);
      });
  };

  useEffect(() => {
    fetch('http://localhost:5000/recipes')
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setRecipes(data);
      })
      .catch((error) => {
        console.error('Error retrieving recipes:', error);
      });
  }, []);

  return (
    <div className="app" style={{ backgroundImage: `url(${backgroundImage})` }}>
      <h1>Bangladeshi Recipes</h1>
      <div className="search-container">
        <div className="search-box">
          <h2>Search by Recipe</h2>
          <input
            type="text"
            placeholder="Enter Recipe Name..."
            value={ingredientName}
            onChange={(e) => setIngredientName(e.target.value)}
          />
          <button onClick={handleIngredientSearch}>Search</button>
        </div>

        <div className="search-box">
          <h2>Search by Serving</h2>
          <input
            type="text"
            placeholder="Enter Servings Number.."
            value={servnum}
            onChange={(e) => setServnum(e.target.value)}
          />
          <button onClick={handleDietSearch}>Search</button>
        </div>

        <div className="search-box">
          <h2>Search by Cook Time</h2>
          <input
            type="text"
            placeholder="Enter Cook Time.."
            value={ct}
            onChange={(e) => setCt(e.target.value)}
          />
          <button onClick={handleCtSearch}>Search</button>
        </div>
      </div>

      <div className="recipe-container">
        <h2>Recipes</h2>
        <div className="recipe-list">
          {searchPerformed && !searchResult ? (
            <div style={{ position: 'relative', zIndex: 9999, display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', fontSize: '18px' }}>
            <div className="recipe-card">
              <h3>No recipe found</h3>
              </div>
              </div>
          ) : (
            recipes.map((recipe, index) => (
              <div className="recipe-card" key={recipe._id}>
                <h3>{recipe.name}</h3>
                <p>
                  <b>Ingredients:</b> {recipe.ingredients}
                </p>
                <p>
                  <b>Serving:</b> {recipe.serving}
                </p>
                <p>
                  <b>Time:</b> {recipe.time} minutes
                </p>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
