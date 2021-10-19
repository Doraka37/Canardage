import { useLocation, useHistory } from "react-router-dom";

function ButtonZoom(props) {

  const history = useHistory();

  function BackToSelec() {

    console.log("hello");
    history.push({
      pathname: '/Game',
    });
  }

  function Play(infos) {
    console.log("je joue la carte : ", infos.name);
  }

  function Discard(infos) {
    console.log("je jette la carte : ", infos.name);
  }

  return (
    <div>
      <button
        className="ZoomButton"
        type="button"
        onClick={() => eval(props.fct)}
      >
        {props.text}

      </button>
    </div>
  )
}

function CardZoom(props) {

  const location = useLocation();

  return (
    <div className="Zoom">
      <div className="bigCard">
        <h1 className="font-link">{location.state.name}</h1>
        <img
          src={location.state.src}
          alt="duck image"
        />
        <p className="font-link"> {location.state.desc} </p>
      </div>
      <ButtonZoom text="Retourner a la main compléte" fct="BackToSelec()" infos={location.state}/>
      <ButtonZoom text="Jouer" fct="Play(props.infos)" infos={location.state}/>
      <ButtonZoom text="Défausser" fct="Discard(props.infos)" infos={location.state}/>
    </div>
  )
}

export default CardZoom;
