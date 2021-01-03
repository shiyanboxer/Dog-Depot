import logo from './logo.svg';
import './App.css';

// mdbreact https://www.npmjs.com/package/mdbreact
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';

// Component files
import Home from './Home.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Home />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="http://shiyanboxer.netlify.app/"
          target="_blank"
          rel="noopener noreferrer"
        >
          By: Shiyan Boxer
        </a>
      </header>
    </div>
  );
}

export default App;
