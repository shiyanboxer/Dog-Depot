import React from "react"
import "../CSS/Footer.css"

class Footer extends React.Component {
    render() {
        return (
            <a
                className="footer"
                href="http://shiyanboxer.netlify.app/"
                target="_blank"
                rel="noopener noreferrer"
            >
                By: Shiyan Boxer
            </a>
        );
    }
}

export default Footer;