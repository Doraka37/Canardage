import { useLocation, useHistory } from "react-router-dom";
import { useState } from 'react';
import walking from '../ressources/template_carte.png'
import dark from '../ressources/template_carte_dark.png'

function CardZoom(props) {

  const location = useLocation();
  const [param, setParam] = useState('');
  const [id, setId] = useState('');
  const [value1, setValue1] = useState('');
  const [value2, setValue2] = useState('');
  const [isClicked, setIsClicked] = useState(["", "", "", "", "", "", ""])

  function validate(id, isDouble) {
    if (value1 == '') {
      return
    }
    if (isDouble == true) {
      console.log("here");
      if (value2 == '') {
        return
      }

    }
    var formdata = new FormData();
    formdata.append('value1', value1)
    formdata.append('value2', value2)
    formdata.append('valueList', '[]')
    formdata.append('playerID', '2')
    formdata.append('cardID', '7')

    var myHeaders = new Headers();
    myHeaders.append('Access-Control-Allow-Origin', '*')

    var requestOptions = {
      method: 'POST',
      redirect: 'follow',
      body: formdata,
      headers: myHeaders
    };

    fetch("http://127.0.0.1:4004/playCard", requestOptions)
      .then(response => {
        console.log("reo: ", response);
        return response.json()
      })
      .then(result => console.log(result.data))
      .catch(error => console.log('error', error));
  }

//#############################################################
  function Rect_case(props) {

    let src = walking
    if (isClicked[props.id] != "") {
      console.log("c noire");
    }
    //className={`circle ${props.clicked ? 'blue': 'black'}`}
    return (
      <div className={"rectangle-selec"} onClick={() => handleClick(props.id, props.type)}>
        <img className={`banner ${isClicked[props.id] ? "black" : ""}`}
          src={src}
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
          setParam('DoubleChoice')
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

  function handleClick(id, type) {
    console.log("placing target at pos: ", id);
    let array = ["", "", "", "", "", "", ""];
    array[id] = "clicked";
    setIsClicked(array)
    if (type == "Double") {
      if (value1 == '') {
        console.log("setting vlaue1");
        setValue1(id)
      }
      else {
        console.log("setting vlaue2");
        setValue2(id)
      }
    }
  }

  function renderSwitch(param) {
    switch(param) {
      case 'SingleChoice':
        return (
            <div className="lay-rectangle">
              <h1 className="title-font"> Please chose where you want to play the card </h1>
              <Rect_case id={1} type={"Single"}/>
              <Rect_case id={2} type={"Single"}/>
              <Rect_case id={3} type={"Single"}/>
              <Rect_case id={4} type={"Single"}/>
              <Rect_case id={5} type={"Single"}/>
              <Rect_case id={6} type={"Single"}/>
              <button className="SelecButton" type="button" onClick={() => setParam('')}>
                Close
              </button>
              <button className="SelecButton" type="button" onClick={() => validate(id, false)}>
                Validate
              </button>
            </div>
        );
        case 'DoubleChoice':
          return (
              <div className="lay-rectangle">
                <h1 className="title-font"> Please chose where you want to place a target </h1>
                <Rect_case id={1} type={"Double"}/>
                <Rect_case id={2} type={"Double"}/>
                <Rect_case id={3} type={"Double"}/>
                <Rect_case id={4} type={"Double"}/>
                <Rect_case id={5} type={"Double"}/>
                <Rect_case id={6} type={"Double"}/>
                <button className="SelecButton" type="button" onClick={() => setParam('')}>
                  Close
                </button>
                <button className="SelecButton" type="button" onClick={() => validate(id, true)}>
                  Validate
                </button>
              </div>
          );
          case 'WalkingDuck':
            return (
                <div className="lay-rectangle">
                  <button className="SelecButton" type="button" onClick={() => setParam('')}>
                    Close
                  </button>
                </div>
            );
            case 'Canarchie':
              return (
                  <div className="lay-rectangle">
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
