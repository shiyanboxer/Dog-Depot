import React from "react"
import Card from "./Card";
import axios from "axios";

class Home extends React.Component{
    // Only is called when Home component is mounted (once)

    state = {
        content : [{"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/alvan-nee-T-0EW-SEbsE-unsplash.jpg", "ImageName": "Img1", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/anoir-chafik-2_3c4dIFYFU-unsplash.jpg", "ImageName": "Img2", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/ash-goldsbrough-v0_MCllHY9M-unsplash.jpg", "ImageName": "Img3", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/chewy-3cAMUE3YAO8-unsplash.jpg", "ImageName": "Img4", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/christopher-ayme-ocZ-_Y7-Ptg-unsplash.jpg", "ImageName": "Img5", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/james-barker-v3-zcCWMjgM-unsplash.jpg", "ImageName": "Img6", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/jay-wennington-CdK2eYhWfQ0-unsplash.jpg", "ImageName": "Img7", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/karl-anderson-jKDFcXwk5Cw-unsplash.jpg", "ImageName": "=Img8", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/michael-oxendine-t7wwffh6x8E-unsplash.jpg", "ImageName": "Img9", "Author": "Shiyan Boxer"}, {"URL": "https://imagerepositorybyshiyanboxer.s3.ca-central-1.amazonaws.com/chewy-b4I9PYFfHVM-unsplash.jpg", "ImageName": "Img10", "Author": "Shiyan Boxer"}],
        receivedResponse:false
    }
    componentDidMount() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:5000/"
        }).then((response)=> {
            if (response.data.isError === false) {
                const new_data = response.data.result

                // this.setState( {content:new_data,receivedResponse:true})
            }
            else {
                alert(response.data.errorMessage)
            }

        })

    }

    render() {
        console.log("State" + this.state.content)
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-3">
                        {this.state.content.map(function (item,index) {
                            return <Card key={index} src={item.URL} title={item.ImageName}></Card>
                        })}

                    </div>
                </div>
            </div>
        );
    }
}

export default Home;
