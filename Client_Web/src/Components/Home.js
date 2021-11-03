import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import Store from '../store';

function Home() {
  const store = Store.getState();

  const history = useHistory();
  const [value, setValue] = useState('');
  const [pseudo, setPseudo] = useState(store.UserInfos.pseudo);
  const [color, setColor] = useState('');
  const [playerList, setPlayerlist] = useState(store.UserInfos.userList);
  const [playerNbr, setplayerNbr] = useState('1');


  function test_req() {
      history.push('/game');
  }

  function handleChange(event) {
    setValue(event.target.value)
  }

  function handleSubmit(event) {
    let action = {
      type: 'SET_PSEUDO',
      value: value
    };
    Store.dispatch(action);
    const list = playerList
    list.push(value)
    setPseudo(value);
    setPlayerlist(list)
    action = {
      type: 'SET_USER_LIST',
      value: list
    }
    Store.dispatch(action);
    setColor("rouge")
    //CALL API POUR PASSER LE PSEUDO
    //history.push('/game');
  }

  function Item(props) {
   return <p className="p-font">{props.value}</p>;
  }

  return (
    <div className="CardZoom">
      <div>
          <h2>Home</h2>
        {pseudo !== '' ?
          <div className="Home">
            <div>
              <button
                type="button"
                onClick={() => test_req()}
              >
                test
              </button>
            </div>
            <p className="p-font"> Bienvenue {pseudo} lors de cette partie vous jouer les canards {color}</p>
            <p className="p-font"> Il y a {playerNbr} joueur·euse.s connecté </p>
            <ul>
              {playerList.map((item) => <Item value={item}/>)}
            </ul>
            <div>
              <button
              className="RuleButton"
                type="button"
                onClick={() => history.push('/Rules')}
              >
                Regles du jeu
              </button>
            </div>
          </div>
            :
          <div className="Home">
            <form onSubmit={handleSubmit}>
              <div>
                <label className="input">
                  <input className="input" type="text" value={value} onChange={handleChange}/>
                </label>
              </div>
              <div>
                <input className="input" type="submit" value="Rejoindre la partie" />
              </div>
            </form>
          </div>
        }
      </div>
    </div>
  );
}

export default Home;
