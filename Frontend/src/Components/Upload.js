import React from "react"
import {MDBContainer, MDBRow, MDBCol, MDBBtn} from 'mdbreact';
import axios from "axios";

class Upload extends React.Component {
    uploader() {
        // Get image parameters by ID and assign variables
        const in_author = document.getElementById("Author").value
        const in_imageName = document.getElementById("ImageName").value
        const in_tag = document.getElementById("Tag").value
        const myFilePath = "C:\\Users\\shiya\\Documents\\UploadImg\\"
        const in_fileName = document.getElementById("FileName").files[0]
        const wholePath = myFilePath + in_fileName.name

        axios({
            method: "POST",
            url: "http://127.0.0.1:5003/upload",
            // Return "data", a dictionary of the users inputs
            data: {
                "Author": in_author,
                "ImageName": in_imageName,
                "Tag": in_tag,
                "FilePath": wholePath,
                "FileName": in_fileName.name
            }
        }).then((response) => {
            // If the is request was successful, display a success message
            if (response.data.isError === false) {
                alert(response.data.successMessage)
            } else {
                alert(response.data.errorMessage)
            }
        })
    }

    // Pass image author, image name, and tag by ID
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
                            <label className="grey-text">
                            </label>
                            <input type="file" id="FileName" className="form-control"/>
                            <div className="text-center mt-4">
                                {/*When button is clicked (onClick) call uploader function*/}
                                <MDBBtn gradient="aqua" rounded size="md" onClick={this.uploader}>Upload</MDBBtn>
                            </div>
                        </form>
                    </MDBCol>
                </MDBRow>
            </MDBContainer>
        );
    }
}

export default Upload;
