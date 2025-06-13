import React, { useState, useEffect } from 'react';

function App() {
  const [assets, setAssets] = useState([]);
  const [newAsset, setNewAsset] = useState({
    name: '',
    type: '',
    status: '',
    location: ''
  });

  useEffect(() => {
    fetch('http://localhost:5000/assets')
      .then(res => res.json())
      .then(data => setAssets(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/assets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newAsset)
    })
    .then(() => {
      // Refresh asset list
      return fetch('http://localhost:5000/assets');
    })
    .then(res => res.json())
    .then(data => setAssets(data));
  };

  return (
    <div className="App">
      <h1>Asset Inventory</h1>
      <form onSubmit={handleSubmit}>
        {/* Form inputs */}
      </form>
      <table>
        {/* Asset listing */}
      </table>
    </div>
  );
}

export default App;