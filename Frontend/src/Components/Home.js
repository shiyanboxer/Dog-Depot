import React from "react"
import Card from "./Card";
import axios from "axios";
import "../CSS/App.css"

class Home extends React.Component {
    // Only is called when Home component is mounted (once)

    state = {
        content: [],
        receivedResponse: false
    }

    componentDidMount() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5001/"
        }).then((response) => {
            if (response.data.isError === false) {
                const new_data = response.data.result
                this.setState({content: new_data, receivedResponse: true})
            } else {
                alert(response.data.errorMessage)
            }
        })
    }

    render() {
        console.log("State" + this.state.content)
        return (
            <div className="container">
                <div className="row">
                    {this.state.receivedResponse ?
                        this.state.content.map((item, index) => (
                            <div className="col-md-4">
                                <Card src={item.URL} title={item.ImageName}></Card>
                            </div>
                        ))
                        :
                        null
                    }
                </div>
            </div>
        );
    }
}

export default Home;
