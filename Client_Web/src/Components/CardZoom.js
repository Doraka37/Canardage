import { useLocation, useHistory } from "react-router-dom";
import { useState } from 'react';
import walking from '../ressources/template_carte.png'
import dark from '../ressources/template_carte_dark.png'
import blue from '../ressources/dos_carte_bleu.png'
import green from '../ressources/dos_carte_vert.png'
import pink from '../ressources/dos_carte_rose.png'
import purple from '../ressources/dos_carte_violet.png'
import yellow from '../ressources/dos_carte_jeune.png'
import orange from '../ressources/dos_carte_orange.png'
import Store from '../store';

function CardZoom(props) {

  const location = useLocation();
  const [param, setParam] = useState('');
  const [id, setId] = useState(0);
  const [value1, setValue1] = useState(0);
  const [value2, setValue2] = useState(0);
  const [valueList, setValueList] = useState(["", "", "", "", "", ""]);
  const [cpt, setCpt] = useState(1);
  const [errMess, setErrMess] = useState("No Error Message");
  const [isClicked, setIsClicked] = useState(["", "", "", "", "", "", ""])
  const history = useHistory();

  function reset() {
    setValue1(0);
    setValue2(0);
    setIsClicked(["", "", "", "", "", "", ""]);
    setValueList(["", "", "", "", "", ""]);
    setCpt(1);
  }

  function validate(id, type) {
    console.log("valuelist: ", valueList);
    console.log("value1: ", value1);
    console.log("value2: ", value2);
    console.log("playerID: ", location.state.playerID);
    console.log("cardID: ", location.state.cardID);
    if (type == "Single" && value1 == 0) {
      console.log("no value1");
      return
    }
    if (type == "Double") {
      console.log("here");
      if (value2 == '') {
        return
      }

    }
    var formdata = new FormData();
    formdata.append('value1', value1)
    formdata.append('value2', value2)
    formdata.append('valueList', valueList)
    formdata.append('playerID', location.state.playerID)
    formdata.append('cardID', location.state.cardID)

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
      .then(result => {
        console.log("he suis le result;error: ", result.Message);
        if (result.status == 300) {
          console.log(result.Message)
          setParam("Error")
          setErrMess(result.Message)
        } else {
          console.log("new_card: ", result.data);
          const store = Store.getState();
          let new_hand = store.UserInfos.hand
          new_hand[location.state.pos - 1] = result.data
          console.log("new_hand: ", new_hand);
          let action = {
            type: 'SET_HAND',
            value: new_hand
          };
          Store.dispatch(action);
          reset()
          //setParam('')
          history.push({
            pathname: '/Game',
          });
        }
      })
      .catch(error => console.log('error oui la bonne'));
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
        <img className={`img-sel ${isClicked[props.id] ? "black" : ""}`}
          src={src}
          alt="duck image"
        />
      </div>
    )
  }
//#############################################################

//#############################################################
  function Color_case(props) {

    let src = props.color;
    return (
      <div className={"rectangle-selec"} onClick={() => handleClick(props.id, props.type)}>
        <img className={`img-sel ${isClicked[props.id] ? "black" : ""}`}
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
      console.log("je joue la carte : ", infos.pos);
      switch(infos.pos) {
        case 1:
          console.log("hello1: ", infos.type);
          setParam(infos.type)
          break;
        case 2:
          console.log("hello2: ", infos.type);
          setParam(infos.type)
          break;
        case 3:
          console.log("hello3: ", infos.type);
          setParam(infos.type)
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
    if (isClicked[id] == "clicked")
      return;
    if (type == "Double") {
      if (value1 == 0) {
        console.log("setting vlaue1");
        setValue1(id)
        let array = ["", "", "", "", "", "", ""];
        array[id] = "clicked";
        setIsClicked(array)
      }
      else if (value2 == 0) {
        console.log("setting vlaue2");
        setValue2(id)
        let array = isClicked;
        array[id] = "clicked";
        setIsClicked(array)
      }
      return;
    }
    if (type == "Canarchie") {
      if (cpt >= 7) {
        return;
      }
      let array = valueList;
      console.log("cpt: ", cpt, " array: ", array);
      array[cpt - 1] = id;
      setValueList(array);
      setCpt(cpt + 1);
      let click = isClicked;
      click[id] = "clicked";
      setIsClicked(click)
      return;
    }
    if (value1 == 0) {
      console.log("setting vlaue1");
      setValue1(id)
      let array = ["", "", "", "", "", "", ""];
      array[id] = "clicked";
      setIsClicked(array)
    }
    console.log("placing target at pos: ", id);
    let array = ["", "", "", "", "", "", ""];
    array[id] = "clicked";
    setIsClicked(array)
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
              <button className="SelecButton" type="button" onClick={() => validate(id, "Single")}>
                Validate
              </button>
            </div>
        );
      case 'DoubleChoice':
        return (
            <div className="lay-rectangle">
              <h1 className="title-font"> Please chose two tiles where you want to play the cards </h1>
              <Rect_case id={1} type={"Double"}/>
              <Rect_case id={2} type={"Double"}/>
              <Rect_case id={3} type={"Double"}/>
              <Rect_case id={4} type={"Double"}/>
              <Rect_case id={5} type={"Double"}/>
              <Rect_case id={6} type={"Double"}/>
              <button className="SelecButton" type="button" onClick={() => setParam('')}>
                Close
              </button>
              <button className="SelecButton" type="button" onClick={() => validate(id, "Double")}>
                Validate
              </button>
              <button className="SelecButton" type="button" onClick={() => reset(id, false)}>
                Reset
              </button>
            </div>
        );
      case 'WalkingDuck':
        return (
            <div className="lay-rectangle">
              <h1 className="title-font"> Please chose which color you wish to revive a duck from </h1>
              <Color_case id={1} color={blue}/>
              <Color_case id={2} color={green}/>
              <Color_case id={3} color={pink}/>
              <Color_case id={4} color={purple}/>
              <Color_case id={5} color={yellow}/>
              <Color_case id={6} color={orange}/>
              <button className="SelecButton" type="button" onClick={() => setParam('')}>
                Close
              </button>
              <button className="SelecButton" type="button" onClick={() => validate(id, "Single")}>
                Validate
              </button>
            </div>
        );
      case 'Canarchie':
        return (
          <div className="lay-rectangle">
            <h1 className="title-font"> {cpt != 7 ? "Please the card you want to place at position" : "Validate or reset"} </h1>
            <Rect_case id={1} type={"Canarchie"}/>
            <Rect_case id={2} type={"Canarchie"}/>
            <Rect_case id={3} type={"Canarchie"}/>
            <Rect_case id={4} type={"Canarchie"}/>
            <Rect_case id={5} type={"Canarchie"}/>
            <Rect_case id={6} type={"Canarchie"}/>
            <button className="SelecButton" type="button" onClick={() => setParam('')}>
              Close
            </button>
            <button className="SelecButton" type="button" onClick={() => validate(id, "Canarchie")}>
              Validate
            </button>
            <button className="SelecButton" type="button" onClick={() => reset(id, false)}>
              Reset
            </button>
          </div>
        );
      case 'Error':
        return (
          <div className="Zoom">
            <div className="errorMess">
              <h1 className="font-link">Impossible de jouer la carte sur les/la case selectionnées</h1>
              <p className="font-link">{errMess}</p>
              <button className="SelecButton" type="button" onClick={() => setParam('')}>
                OK
              </button>
            </div>
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
