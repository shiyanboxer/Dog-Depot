import React from "react"
import axios from "axios";
import NavBar from "./NavBar";
import Card from "./Card";
import "../CSS/App.css"
import "../CSS/Navbar.css";


class Home extends React.Component {
    // Use state to see when content changes
    state = {
        content: [],
        receivedResponse: false
    }

    // Used by nav bar that calls Search API each time a the search changes
    handleSearchRequest(e) {
        const search_text = e.target.value
        axios({
            method: "POST",
            // url: "http://127.0.0.1:5000/search",
            url: "https://dog-depot-shiyan.herokuapp.com/search",
            // Return "data" a dictionary which contains a single key value search_text that is the content in the search bar
            data: {"search_text": search_text}
        }).then((response) => {
            if (response.data.isError === false) {
                // If no error sending request, then set "new_data" to response.data.result and change "content" state to "new_data"
                const new_data = response.data.result
                this.setState({content: new_data})
            } else {
                alert(response.data.errorMessage)
            }
        })
    }

    // Only is called when Home component mounted (only once)
    componentDidMount() {
        axios({
            method: "GET",
            url: "https://dog-depot-shiyan.herokuapp.com/"
            // url: "http://127.0.0.1:5000/"
        }).then((response) => {
            if (response.data.isError === false) {
                const new_data = response.data.result
                // Same as handleSearchRequest but change "receivedResponse" to true
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
                            {/*functionCall bind this with handleSearchRequest*/}
                            <NavBar functionCall={this.handleSearchRequest.bind(this)}></NavBar>
                        </div>
                    </div>
                </div>
                <div className="container">
                    <div className="row">
                        {
                            // Ternary operator, if state.receivedResponse is true, display images in cards, else null
                            this.state.receivedResponse ?
                                this.state.content.map((item, index) => (
                                    <div className="col-md-4">
                                        {/*Display image and title*/}
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
