import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams
} from "react-router-dom";
import Game from './Components/game'

function sayHello() {
  alert('You clicked me!');
}

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
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

function Home() {
  return <h2>Home</h2>;
}

export default App;
