import './CSS/App.css';
import {BrowserRouter} from "react-router-dom";
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';
import Navbar from "./Components/NavBar";
import Routes from "./Components/Routes"
import Footer from "./Components/Footer";

function App() {
    return (
        <div>
            <BrowserRouter>
                <div className="App">
                    <Navbar/>
                    <Routes/>
                    <Footer/>
                </div>
            </BrowserRouter>
        </div>
    );
}

export default App;