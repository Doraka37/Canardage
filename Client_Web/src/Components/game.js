import React, { useState } from 'react';

import en_joue from '../ressources/en_joue.png'
import walking_duck from '../ressources/walking_duck.png'
import dispersion from '../ressources/dispersion.png'
import a_couvert from '../ressources/a_couvert.png'
import banzai from '../ressources/banzai.png'
import canarchie from '../ressources/canarchie.png'
import double_viseur from '../ressources/double_viseur.png'
import en_avant_marche from '../ressources/en_avant_marche.png'
import palme_arriere from '../ressources/palme_arriere.png'
import palme_avant from '../ressources/palme_avant.png'
import pan from '../ressources/pan.png'
import peace_and_love from '../ressources/peace_and_love.png'
import planque from '../ressources/planque.png'
import rectifier_tir_droite from '../ressources/rectifier_tir_droite.png'
import rectifier_tir_gauche from '../ressources/rectifier_tir_gauche.png'
import tireur_delite from '../ressources/tireur_delite.png'
import tu_louches from '../ressources/tu_louches.png'
import canardage from '../ressources/canardage.png'

import plateau from '../ressources/plateau.png'

import list from '../ressources/test.json'
import Card from './Card'
import Store from '../store';

function Game() {
  const store = Store.getState();
  const [hand, setHand] = useState(store.UserInfos.hand);
  var array = [];

  array.push(pan);
  array.push(en_joue);
  array.push(tu_louches);
  array.push(tireur_delite);
  array.push(rectifier_tir_droite);
  array.push(rectifier_tir_gauche);
  array.push(double_viseur);
  array.push(canardage);
  array.push(planque);
  array.push(a_couvert);
  array.push(canarchie);
  array.push(dispersion);
  array.push(walking_duck);
  array.push(peace_and_love);
  array.push(en_avant_marche);
  array.push(banzai);
  array.push(palme_avant);
  array.push(palme_arriere);

  console.log("game pseduo is: ", store.UserInfos.playerID);
  hand[0] = 9
  hand[1] = 3
  console.log("test: ", hand[0]);
  return (
    <div className="App">
      <Card cardInfo={list.cards[hand[0]]} array={array} playerID={store.UserInfos.playerID} pos={1} hand={hand} className="rectangle"/>
      <Card cardInfo={list.cards[hand[2]]} array={array} playerID={store.UserInfos.playerID} pos={3} hand={hand} className="rectangle2"/>
      <Card cardInfo={list.cards[hand[1]]} array={array} playerID={store.UserInfos.playerID} pos={2} hand={hand} className="rectangle3"/>
    </div>
  )
}

export default Game;
