import React from "react"
import {MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavItem, MDBNavLink, MDBNavbarToggler, MDBCollapse, MDBFormInline, MDBDropdown, MDBDropdownToggle, MDBDropdownMenu, MDBDropdownItem} from "mdbreact";
import "../CSS/Navbar.css"

class NavBar extends React.Component{
  state = {
  isOpen: false
};

toggleCollapse = () => {
  this.setState({isOpen: !this.state.isOpen}
  );
}

  render() {
    return(
         // background color of nav bar
        <MDBNavbar color="black" expand="lg">
        <MDBNavbarBrand>
          <strong className="white-text">Image Repository of Dogs</strong>
        </MDBNavbarBrand>
        <MDBNavbarToggler className="toggle" onClick={this.toggleCollapse} />
        <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
          <MDBNavbarNav left>
            <MDBNavItem active>
              <MDBNavLink to="/">Home</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/upload">Upload</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/search">Search</MDBNavLink>
            </MDBNavItem>
          </MDBNavbarNav>

        </MDBCollapse>
      </MDBNavbar>
    )
  }
}

export default NavBar;