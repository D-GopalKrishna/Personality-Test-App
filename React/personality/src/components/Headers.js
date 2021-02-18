import React from 'react';
import {Navbar, Nav} from 'react-bootstrap';
import {Link} from 'react-router-dom';


const Headers = ({userData}) => {

    const onClick = (e) => {

    }




    return (
        <div>
            <Navbar collapseOnSelect expand="sm" bg="dark"  variant="dark">
                <Link className="links" to="/"><Navbar.Brand>
                Personality Test
                </Navbar.Brand></Link>
                {/* <div className="NavBar">
                    <Link className="links" to="/">Home</Link>
                    <Link className="links" to="/">Get Your Results</Link>
                    <Link className="links" to="/">Take Test</Link>
                </div> */}

                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link><Link to="/resultentername" style={{color:'#bdc1c7', textDecoration:'none'}} onClick={onClick} >Result</Link></Nav.Link>
                        <Nav.Link><Link to="/entername" style={{color:'#bdc1c7', textDecoration:'none'}} onClick={onClick} >Test</Link></Nav.Link>
                        {/* <Nav.Link>Test</Nav.Link>
                        <Nav.Link>Test</Nav.Link> */}

                    </Nav>
                    
                </Navbar.Collapse>
                
            </Navbar>

            


        </div>
    )
}

export default Headers
