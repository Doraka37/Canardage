import React, { useState } from 'react';

import duck from '../ressources/duck0.jpg'
import colver from '../ressources/colver.jpg'
import barbarie from '../ressources/Canards_de_Barbarie.jpg'
import walking from '../ressources/en_joue.png'
import en_joue from '../ressources/walking_duck.png'
import dispersion from '../ressources/dispersion.png'
import list from '../ressources/test.json'
import Card from './Card'
import Store from '../store';

function Game() {
  const store = Store.getState();
  const [hand, setHand] = useState(store.UserInfos.hand);
  var array = [];

  array.push(walking);
  array.push(dispersion);
  array.push(en_joue);

  console.log("game pseduo is: ", store.UserInfos.pseudo);
  console.log("test: ", hand[0]);
  return (
    <div className="App">
      <Card cardInfo={list.cards[hand[0]]} array={array} playerID={2} pos={1} className="rectangle"/>
      <Card cardInfo={list.cards[hand[2]]} array={array} playerID={2} pos={3} className="rectangle2"/>
      <Card cardInfo={list.cards[hand[1]]} array={array} playerID={2} pos={2} className="rectangle3"/>
    </div>
  )
}

export default Game;
