import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams
} from "react-router-dom";

function sayHello() {
  alert('You clicked me!');
}

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/Test">
            <Test/>
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

function Test() {
  return (
    <div className="App">
      <div className="rectangle">
      </div>
      <div className="rectangle2">
      </div>
      <div className="rectangle3">
      </div>
    </div>
  )
}

export default App;
