import React from 'react'
import {Link, useHistory} from 'react-router-dom';
import { useState, useEffect } from 'react'
import {Jumbotron, Container} from 'react-bootstrap';

import './styling/TestEnterName.css';

const TaketestButton = ({userData}) => {
    let history = useHistory();

    let hrefy = String(window.location.href).split('/')
    let hrefy_name = hrefy[hrefy.length - 1]
    console.log(hrefy[hrefy.length - 1])

    



    const onClick = () => {
        let i, gotit;
        for (i in userData){
            if (userData[i].username==hrefy_name){

                let user_urlkey = userData[i].url_key;
                history.push(`/test/${user_urlkey}`);
                // gotit = 'Gotit';
            }
        }
    }


    return (
        <div>
            <Jumbotron fluid className="jumboStyle">
                <Container>                   

                    <div className="NameEnter">
                        <p>This test may take 10-30min. </p>
                        <button onClick={onClick} className="SubmitText">Take Test</button>
                    </div>
                    
                </Container>

            </Jumbotron>
            
        </div>
    )
}

export default TaketestButton
