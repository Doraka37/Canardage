import list from '../ressources/test.json'
import Card from './Card'
import duck from '../ressources/duck0.jpg'
import colver from '../ressources/colver.jpg'
import barbarie from '../ressources/Canards_de_Barbarie.jpg'
import FlatList from 'flatlist-react';

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

function Item(props) {
  console.log("props: ", props);
  var src = props.array[props.value.src]

  return (
    <div className="rule-rectangle">
      <h1 className="font-link-title">{props.value.name}</h1>
      <img className="img-rule"
        src={src}
        alt="duck image"
      />
    </div>
  );
}

function Rules() {

  console.log("list: ", list);
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
  //const card_list = JSON.parse(list.cards);

  return (
    <div className="def">
      <div>
        <h1 className="rule-title-font">Principe du jeu</h1>
        <p className="rule-font">
          Les canards barbotent en file indienne dans un ordre sans cesse chamboulé par les joueurs.
          Mais personne n est en sécurité dans ces eaux mitaillées et chacun manoeuvre en évitant de stationner dans une ligne de tir !
          Le dernier canard survivant sera le gagnant !
        </p>
        <h2 className="rule-title-font">Deroulement de la partie</h2>
        <p className="rule-font">
          Le jouer dont le canard est en tête de la ligne commence.
          Quand vient sont tour, un joueur doit:
            Jouer une des cartes Action qu il a en main (même si cela nuit à son jeu !), il recoit ensuite une nouvelle carte.
            Si il ne peux jouer aucune carte, il peu se défausser d une carte pour terminer son tours et recevoir une nouvelle carte
        </p>
      </div>
      <div className="line">
        <h3 className="rule-title-font">Liste des cartes</h3>
        {list.cards.map((item) => <Item value={item} array={array}/>)}
      </div>
    </div>
  )
}

export default Rules;
