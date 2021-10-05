import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

function Home() {
  const history = useHistory();
  const [value, setValue] = useState('');

  function handleChange(event) {
    setValue(event.target.value)
  }

  function handleSubmit(event) {
    //alert('Bravo vous étes un fils de pute : ' + value);
    //event.preventDefault();
    //CALL API POUR PASSER LE PSEUDO
    history.push('/game');
  }



  return (
    <div className="App">
      <h2>Home</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Nom :
          <input type="text" value={value} onChange={handleChange}/>
        </label>
        <input type="submit" value="Envoyer" />
      </form>
    </div>
  );
}

export default Home;
