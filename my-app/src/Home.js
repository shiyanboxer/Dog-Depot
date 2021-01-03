import React, { Component } from "react";
// import React, { Fragment } from "react";
import './App.css';
import { MDBCol } from "mdbreact";
import { MDBBtn } from "mdbreact";
// import axios from "axios"

class Home extends Component {
  render() {
   return (
    <MDBCol md="6">
      <input className="form-control" type="text" placeholder="Search" aria-label="Search" />
    </MDBCol>
  );
  }
}
export default Home;