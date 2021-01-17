import React from "react"
import axios from "axios"
import {DropzoneArea} from 'material-ui-dropzone'
import { MDBContainer, MDBRow, MDBCol, MDBBtn, MDBCard, MDBCardBody, MDBIcon } from 'mdbreact';
var FormData = require('form-data');

class Upload extends React.Component{

    constructor(props){
        super(props);
        this.state = {
          files: []
        };
      }

      handleClick(e){
        e.preventDefault()
        const data = new FormData();
        const imagename = document.getElementById("name").value
        const author = document.getElementById("author").value
        const tag = document.getElementById("tag").value
        data.append('image', this.state.files[0]);

        axios({
            method:"POST",
            url:"https://dog-depot-shiyan.herokuapp.com/upload?imagename="+imagename+"&author="+author+"&tag="+tag,
            // url:"https://dog-depot-shiyan.herokuapp.com/upload?imagename="+imagename+"&author="+author+"&tag="+tag,
            data: data
            }).then((resp)=>{
                const data = resp.data
                if(data.isError){
                    alert(data.errorMessage)
                }
                else{
                    alert(data.successMessage)
                }

            })

      }
      handleChange(files){
        this.setState({
          files: files
        });

      }
      render(){
        return (
        <div className="container">
        <MDBContainer style={{"marginLeft":"25rem"}}>
                 <MDBRow>
                     <MDBCol md="9">
                     <MDBCard>
                         <MDBCardBody>
                              <form>
                             <p className="h4 text-center py-4">Upload a new Image</p>
                             <label
                            htmlFor="defaultFormCardNameEx"
                            className="grey-text font-weight-light"
                            >
                            Image name
                            </label>
                            <input
                            type="text"
                            id="name"
                            className="form-control"
                            />

                            <label
                            htmlFor="defaultFormCardEmailEx"
                            className="grey-text font-weight-light"
                            >
                            Author
                            </label>
                            <input
                            type="text"
                            id="author"
                            className="form-control"
                            />

                            <label
                            htmlFor="defaultFormCardEmailEx"
                            className="grey-text font-weight-light"
                            >
                            Tag
                            </label>
                            <input
                            type="text"
                            id="tag"
                            className="form-control"
                            />
                            <br/>
                        </form>
                        </MDBCardBody>
                    </MDBCard>
                    </MDBCol>
                </MDBRow>
                <MDBRow>
                    <MDBCol md="9">
                    <DropzoneArea onChange={this.handleChange.bind(this)}/>
                    <button onClick={this.handleClick.bind(this)} className="btn btn-primary">Upload</button>
                    </MDBCol>
                </MDBRow>

            </MDBContainer>

            </div>
        )
      }
}

export default Upload;