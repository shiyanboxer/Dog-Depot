import React from "react"
import {Route, Switch} from "react-router-dom"
import Home from "./Home"
import Upload from "./Upload";

class Routes extends React.Component{
    render() {
        return (
            <div>
                <Switch>
                <Route exact path="/" component={Home}></Route>
                <Route exact path="/upload" component={Upload}></Route>
                </Switch>
            </div>
        );
    }
}

export default Routes;
