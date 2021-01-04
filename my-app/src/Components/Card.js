import React from "react"
import { MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol } from 'mdbreact';

class Card extends React.Component{
    render() {
        return (
            <MDBCol>
              <MDBCard style={{ width: "22rem", height: "20rem" }}>
                <MDBCardImage className="img-fluid" src={this.props.src} waves />
                <MDBCardBody>
                  <MDBCardTitle>{this.props.title}</MDBCardTitle>
                  <MDBCardText>
                  </MDBCardText>
                </MDBCardBody>
              </MDBCard>
            </MDBCol>
        );
    }
}

export default Card;
