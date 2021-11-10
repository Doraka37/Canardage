import { useHistory } from 'react-router-dom';

function Card(props) {
  const history = useHistory();
  console.log("src: ", props.cardInfo.src);
  var src = props.array[props.cardInfo.src]
  function handleClick(cardID, name, src, playerID, pos, type, hand) {
          console.log(cardID);
          var data = [cardID, name, src]
          console.log(data);
          history.push({
            pathname: '/CardZoom',
            state: {name: name, src: src, cardID: cardID, playerID: playerID, pos: pos, type: type, hand: hand}
          });
  }
  return (
    <div className={props.className} onClick={() => handleClick(props.cardInfo.id, props.cardInfo.name, src, props.playerID, props.pos, props.cardInfo.type, props.hand)}>
      <h1 className="font-link-title">{props.cardInfo.name}</h1>
      <img className="img-test"
        src={src}
        alt="duck image"
      />
    </div>
  )
}

export default Card;
