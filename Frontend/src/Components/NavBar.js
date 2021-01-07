import React from "react"
import {MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavItem, MDBNavLink, MDBNavbarToggler, MDBCollapse, MDBFormInline, MDBDropdown, MDBDropdownToggle, MDBDropdownMenu, MDBDropdownItem} from "mdbreact";

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
        <MDBNavbar color="black" expand="md">
        <MDBNavbarBrand>
          <strong className="white-text">Image Repository of Dogs</strong>
        </MDBNavbarBrand>
        <MDBNavbarToggler onClick={this.toggleCollapse} />
        <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
          <MDBNavbarNav left>
            <MDBNavItem active>
              <MDBNavLink to="/">Home</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/upload">Upload</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/delete">Delete</MDBNavLink>
            </MDBNavItem>
          </MDBNavbarNav>
          <MDBNavbarNav right>

            <MDBNavItem>
              <MDBFormInline waves>
                <div className="searchBar" >
                  <input className="form-control mr-sm-2" type="text" placeholder="Search by author, image name, or tag" aria-label="Search" />
                </div>
              </MDBFormInline>
            </MDBNavItem>
          </MDBNavbarNav>
        </MDBCollapse>
      </MDBNavbar>
    )
  }
}

export default NavBar;