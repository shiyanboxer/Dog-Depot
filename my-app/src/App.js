import logo from './logo.svg';
import './App.css';
import {BrowserRouter} from "react-router-dom";
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';
import Navbar from "./Components/NavBar";
import Routes from "./Components/Routes"

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <div className="App">
          <Navbar/>
          <Routes/>
          {/* <Footer/> */}
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;