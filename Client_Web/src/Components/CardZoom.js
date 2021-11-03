import { useLocation, useHistory } from "react-router-dom";
import { useState } from 'react';
import walking from '../ressources/template_carte.png'

function CardZoom(props) {

  const location = useLocation();
  const [param, setParam] = useState('');

//#############################################################
  function Rect_case(props) {
    function handleClick(id) {
            console.log("placing target at pos: ", id);
    }

    return (
      <div className="rectangle-selec" onClick={() => handleClick(props.id)}>
        <img className="img-test"
          src={walking}
          alt="duck image"
        />
      </div>
    )
  }
//#############################################################

//#############################################################
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
      switch(infos.name) {
        case "Canard1":
          console.log("hello");
          setParam(infos.name)
          break;
        case "Canard2":
          // code block
          break;
        default:
          // code block
      }
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
//#############################################################

  function handleClick(id) {
          console.log("placing target at pos: ", id);
  }

  function renderSwitch(param) {
    switch(param) {
      case 'Canard1':
        return (
            <div className="lay-rectangle">
              <h1 className="title-font"> Please chose where you want to place a target </h1>
              <Rect_case id={1}/>
              <Rect_case id={2}/>
              <Rect_case id={3}/>
              <Rect_case id={4}/>
              <Rect_case id={5}/>
              <Rect_case id={6}/>
              <button className="SelecButton" type="button" onClick={() => setParam('')}>
                Close
              </button>
            </div>
        );
      default:
      return (
        <div className="Zoom">
          <div className="bigCard">
            <h1 className="font-link">{location.state.name}</h1>
            <img className="img-zoom"
              src={location.state.src}
              alt="duck image"
            />
          </div>
          <ButtonZoom text="Retourner a la main compléte" fct="BackToSelec()" infos={location.state}/>
          <ButtonZoom text="Jouer" fct="Play(props.infos)" infos={location.state}/>
          <ButtonZoom text="Défausser" fct="Discard(props.infos)" infos={location.state}/>
        </div>
      );
    }
  }

  return (
    <div className="Zoom">
      {renderSwitch(param)}
    </div>
  )
}

export default CardZoom;
