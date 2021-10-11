import list from '../ressources/Card_list.json'
import Card from './Card'
import duck from '../ressources/duck0.jpg'
import colver from '../ressources/colver.jpg'
import barbarie from '../ressources/Canards_de_Barbarie.jpg'
import FlatList from 'flatlist-react';

function Item(props) {
  console.log("props: ", props);
  var src = props.array[props.value.src]

  return (
    <div className="rule-rectangle">
      <h1 className="font-link-title">{props.value.name}</h1>
      <img
        src={src}
        alt="duck image"
      />
      <p className="font-link"> {props.value.desc} </p>
    </div>
  );
}

function Rules() {

  console.log("list: ", list);
  var array = [];
  array.push(duck);
  array.push(colver);
  array.push(barbarie);
  //const card_list = JSON.parse(list.cards);

  return (
    <div className="App">
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
          1) Jouer une des cartes Action qu il a en main (même si cela nuit à son jeu !)
          2)
      </p>
      <h3 className="rule-title-font">Liste des cartes</h3>
      {list.cards.map((item) => <Item value={item} array={array}/>)}
    </div>
  )
}

export default Rules;
