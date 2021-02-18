import React from 'react'
import {Jumbotron, Container, Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';

import './styling/IntroBlock.css';


const IntroBlock = () => {
    return (
        <div className="mainDiv">
            <Jumbotron className="jumboStyle">
                <Container className="cont">
                    <h1>This is a Personality test horizon</h1>
                    <p>Welcome! Checkout your very own personality type by answering few questions. Click "Take Test" to start.</p>
                    <br/>
                    <Link to="/entername"><Button style={{background:'#6c7680'}}>Take Test</Button></Link>
                </Container>
            </Jumbotron>
        </div>
    )
}

export default IntroBlock
