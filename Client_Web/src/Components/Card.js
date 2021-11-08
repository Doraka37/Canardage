import { useHistory } from 'react-router-dom';

function Card(props) {
  const history = useHistory();
  var src = props.array[props.src]
  function handleClick(desc, name, src) {
          console.log(desc);
          var data = [desc, name, src]
          console.log(data);
          history.push({
            pathname: '/CardZoom',
            state: {name: name, src: src, desc: desc}
          });
  }
  return (
    <div className={props.className} onClick={() => handleClick(props.text, props.name, src)}>
      <h1 className="font-link-title">{props.name}</h1>
      <img className="img-test"
        src={src}
        alt="duck image"
      />
    </div>
  )
}

export default Card;
