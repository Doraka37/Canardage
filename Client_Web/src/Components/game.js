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
  var array = [];
  array.push(walking);
  array.push(dispersion);
  array.push(en_joue);

  const store = Store.getState();
  console.log("game pseduo is: ", store.UserInfos.pseudo);
  return (
    <div className="App">
      <Card text={list.cards[0].desc} src={list.cards[0].src} array={array} name={list.cards[0].name} className="rectangle"/>
      <Card text={list.cards[2].desc} src={list.cards[2].src} array={array} name={list.cards[2].name} className="rectangle2"/>
      <Card text={list.cards[1].desc} src={list.cards[1].src} array={array} name={list.cards[1].name} className="rectangle3"/>
    </div>
  )
}

export default Game;
