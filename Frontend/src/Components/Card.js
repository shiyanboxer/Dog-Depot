import React from "react"
import {MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol} from 'mdbreact';
import "../CSS/Card.css"

class Card extends React.Component {
    render() {
        return (
            <MDBCol>
                <MDBCard className="card">
                    <MDBCardImage className="img-fluid" id="card-img" src={this.props.src} waves/>
                    <MDBCardBody>
                        <MDBCardTitle className="cardText">{this.props.title}</MDBCardTitle>
                        <MDBCardText>
                        </MDBCardText>
                    </MDBCardBody>
                </MDBCard>
            </MDBCol>
        );
    }
}

export default Card;
