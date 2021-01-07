import React from "react";
import {MDBContainer, MDBRow, MDBCol, MDBBtn} from 'mdbreact';
import axios from "axios";
import "../CSS/Search.css"
import Card from "./Card";

// https://mdbootstrap.com/docs/react/forms/search/

class Search extends React.Component {
    // When the search button is clicked, send info in text to backend and render results on screen
    state = {
        content: [],
        receivedResponse: false
    }

    search() {
        // Assign variables to input values given by user
        const in_author = document.getElementById("Author").value
        const in_imageName = document.getElementById("ImageName").value
        const in_tag = document.getElementById("Tag").value

        // Check to see it works by printing results in console on click
        // console.log(in_author + in_imageName + in_tag)

        axios({
            method: "POST",
            url: "http://127.0.0.1:5002/search",
            data: {"Author": in_author, "ImageName": in_imageName, "Tag": in_tag}
        }).then((response) => {
            // Notify user with results of action (successMessage and errorMessage are defined in Search.py)
            if (response.data.isError === false) {
                // If no error with the response from the API, the print an success message
                // And set new data to result, content to new_data, and recivedResponse to true
                alert(response.data.successMessage)
                const new_data = response.data.result
                this.setState({content: new_data, receivedResponse: true})
            } else {
                // If there is an error with the response from the API, the print an error message
                alert(response.data.errorMessage)
            }
        })
    }

    render() {
        return (
            <MDBContainer className="upload">
                <MDBRow>
                    <MDBCol md="12">
                        <form>
                            <label className="grey-text">
                                Author
                            </label>
                            <input type="text" id="Author" className="form-control"/>
                            <br/>
                            <label className="grey-text">
                                Image Name
                            </label>
                            <input type="text" id="ImageName" className="form-control"/>
                            <br/>
                            <label className="grey-text">
                                Tag
                            </label>
                            <input type="text" id="Tag" className="form-control"/>
                            <br/>
                            <div className="text-center mt-4">
                                <MDBBtn gradient="aqua" rounded size="md" onClick={this.search}>Search</MDBBtn>
                            </div>
                        </form>
                    </MDBCol>
                </MDBRow>
                <MDBRow>
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
                </MDBRow>
            </MDBContainer>
        );
    }
}

export default Search;