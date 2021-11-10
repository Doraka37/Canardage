import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import Store from '../store';

function Home() {
  const store = Store.getState();

  const history = useHistory();
  const [value, setValue] = useState('');
  const [pseudo, setPseudo] = useState(store.UserInfos.pseudo);
  const [color, setColor] = useState('');
  const [playerID, setPlayerID] = useState(0);
  const [playerList, setPlayerlist] = useState(store.UserInfos.userList);
  const [playerNbr, setplayerNbr] = useState('1');
  const [isStarted, setIsStarted] = useState(false);

  async function start_game() {
    var started = false;
    var move = false;
    var formdata = new FormData();
    var list = []
    var hand = []
    formdata.append('playerID', playerID)
    formdata.append('getCard', true)

    var myHeaders = new Headers();
    myHeaders.append('Access-Control-Allow-Origin', '*')


    var requestOptions = {
      method: 'POST',
      redirect: 'follow',
      body: formdata,
      headers: myHeaders
    };

      let time=setInterval(function(){
        if (started == true) {
          if (move == false) {
            move = true;
            history.push('/game');
          }
          return
        }
        fetch("http://127.0.0.1:4004/userAfk", requestOptions)
          .then(response => {
            console.log("userafk: ", response);
            return response.json()
          })
          .then(result => {
            console.log("result: ", result);
            if (result.started == true) {
              started = true
              hand[0] = result.card1
              hand[1] = result.card2
              hand[2] = result.card3
              let action = {
                type: 'SET_HAND',
                value: hand
              };
              Store.dispatch(action);
            }
            for (var i = 0; i < result.data.length; i++) {
              if (result.data[i].id != 0) {
                list.push(result.data[i].name)
              }
            }
            setPlayerlist(list)
            list = []
          })
          .catch(error => console.log('error oui la bonne: ', error));
          if (started == true) {
            clearInterval(time)
            history.push('/game');
          }
      },5000);
  }

  function add_user(tmpPseudo) {
    var list = []
    console.log("pseudo: ", tmpPseudo);
    var formdata = new FormData();
    formdata.append("name", tmpPseudo)

    var myHeaders = new Headers();
    myHeaders.append('Access-Control-Allow-Origin', '*')

    var requestOptions = {
      method: 'POST',
      redirect: 'follow',
      body: formdata,
      headers: myHeaders
    };
    fetch("http://127.0.0.1:4004/addUsers", requestOptions)
      .then(response => {
        console.log("reo: ", response);
        return response.json()
      })
      .then(result => {
        console.log("result: ", result);
        for (var i = 0; i < result.data.length; i++) {
          if (result.data[i].name == value) {
            setPlayerID(result.data[i].id)
            setColor(result.data[i].color)
            start_game()
          }
          if (result.data[i].id != 0) {
            list.push(result.data[i].name)
          }
        }
        setPlayerlist(list)
        list = []
      })
      .catch(error => console.log('error oui la bonne: ', error));
  }

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
    add_user(value)
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
            <p className="p-font"> Il y a {playerList.length} joueur·euse.s connecté </p>
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
