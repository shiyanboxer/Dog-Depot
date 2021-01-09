import React from "react"
import axios from "axios";
import NavBar from "./NavBar";
import Card from "./Card";
import "../CSS/App.css"
import "../CSS/Navbar.css";

class Home extends React.Component {
    // Only is called when Home component is mounted (once)

    state = {
        content: [],
        receivedResponse: false
    }

    handleSearchRequest(e) {
        const search_text = e.target.value
        axios({
            method: "POST",
            url: "http://127.0.0.1:5002/search",
            data: {"search_text": search_text}
        }).then((response) => {
            if (response.data.isError === false) {
                const new_data = response.data.result
                console.log(new_data)
                this.setState({content: new_data})
            } else {
                alert(response.data.errorMessage)
            }
        })

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
        return (
            <div>
                <div className="container-fluid">
                    <div className="row">
                        <div className="col-md-12">
                            <NavBar functionCall={this.handleSearchRequest.bind(this)}></NavBar>
                        </div>
                    </div>
                </div>

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
            </div>
        );
    }
}

export default Home;
