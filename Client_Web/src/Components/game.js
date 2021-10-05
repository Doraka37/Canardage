import duck from '../ressources/duck0.jpg'
import colver from '../ressources/colver.jpg'
import barbarie from '../ressources/Canards_de_Barbarie.jpg'
import list from '../ressources/test.json'
import { useHistory } from 'react-router-dom';



function Card(props) {
  const history = useHistory();

  function handleClick() {
          console.log('in cardClick');
          history.push('/home');
  }

  return (
    <div className={props.className} onClick={handleClick}>
      <h1 className="font-link">{props.name}</h1>
      <img
        src={props.array[props.src]}
        alt="duck image"
      />
      <p className="font-link"> {props.text} </p>
    </div>
  )
}

function Game() {
  var array = [];
  array.push(duck);
  array.push(colver);
  array.push(barbarie);

  return (
    <div className="App">
      <Card text={list.cards[0].desc} src={list.cards[0].src} array={array} name={list.cards[0].name} className="rectangle"/>
      <Card text={list.cards[1].desc} src={list.cards[1].src} array={array} name={list.cards[1].name} className="rectangle2"/>
      <Card text={list.cards[2].desc} src={list.cards[2].src} array={array} name={list.cards[2].name} className="rectangle3"/>
    </div>
  )
}

export default Game;
