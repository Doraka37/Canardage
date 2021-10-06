import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import Game from './Components/game'
import Home from './Components/Home'
import CardZoom from './Components/CardZoom'

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/CardZoom">
            <CardZoom/>
          </Route>
          <Route path="/Game">
            <Game/>
          </Route>
          <Route path="/">
            <Home/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
