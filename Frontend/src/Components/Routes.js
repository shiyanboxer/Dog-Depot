import React from "react"
import {Route, Switch} from "react-router-dom"
import Home from "./Home"
import Upload from "./Upload";
import Search from "./Search";

class Routes extends React.Component {
    render() {
        return (
            <div>
                <Switch>
                    <Route exact path="/" component={Home}></Route>
                    <Route exact path="/upload" component={Upload}></Route>
                    <Route exact path="/search" component={Search}></Route>
                </Switch>
            </div>
        );
    }
}

export default Routes;
