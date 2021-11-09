import { useHistory } from 'react-router-dom';

function Card(props) {
  const history = useHistory();
  var src = props.array[props.cardInfo.src]
  function handleClick(cardID, name, src, playerID, pos, type) {
          console.log(cardID);
          var data = [cardID, name, src]
          console.log(data);
          history.push({
            pathname: '/CardZoom',
            state: {name: name, src: src, cardID: cardID, playerID: playerID, pos: pos, type: type}
          });
  }
  return (
    <div className={props.className} onClick={() => handleClick(props.cardInfo.id, props.cardInfo.name, src, props.playerID, props.pos, props.cardInfo.type)}>
      <h1 className="font-link-title">{props.cardInfo.name}</h1>
      <img className="img-test"
        src={src}
        alt="duck image"
      />
    </div>
  )
}

export default Card;
