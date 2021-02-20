import React from 'react'
import {Link} from 'react-router-dom'
import {Jumbotron, Container, Table} from 'react-bootstrap';
import { useState, useEffect } from 'react'

import './styling/Results.css';

const Results = ({userData}) => {
    // console.log(userData[0])
    // console.log("hi")
    let hrefy = String(window.location.href).split('/')
    // hrefy = 
    console.log(hrefy[hrefy.length - 1])
    // console.log('http://127.0.0.1:8000/personality_api/userdata/'+hrefy[hrefy.length - 1])


    const [userDataSpecific, setuserDataSpecific] = useState([])


    // GET
    useEffect(() => {
        const getUserDataSpecific = async () => {
        const userDataSpecificFromServer = await fetchUserDataSpecific()
        setuserDataSpecific(userDataSpecificFromServer)
        }
        getUserDataSpecific()
    }, [])

    const fetchUserDataSpecific = async () => {
        const res = await fetch('http://127.0.0.1:8000/personality_api/userdata/'+hrefy[hrefy.length - 1])
        const data = await res.json()

        return data
    }
    console.log(userDataSpecific)
    console.log(userDataSpecific.personality_type)












    return (
        <div>
            <Jumbotron className="jumboStyle">
                <Container>
                    <h5>Hello! {userDataSpecific.username}.</h5>
                    <p>According to the ML model your data was passed through, you come under Personality type - {userDataSpecific.personality_type}. All the metrics are out of 10. </p>
                    <p>Your Score in the test is :</p>

                    <Table striped bordered hover variant="dark" style={{textAlign:'center'}}>
                        <thead>
                            <tr>
                            <th>Characteristics</th>
                            <th>Your Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Extroversion</td>
                                <td>{userDataSpecific.extroversion_score}</td>
                            </tr>
                            <tr>
                                <td>Neurotic</td>
                                <td>{userDataSpecific.neurotic_score}</td>
                            </tr>
                            <tr>
                                <td>Agreeable</td>
                                <td>{userDataSpecific.agreeable_score}</td>
                            </tr>
                            <tr>
                                <td>Conscientious</td>
                                <td>{userDataSpecific.conscientious_score}</td>
                            </tr>
                            <tr>
                                <td>Open</td>
                                <td>{userDataSpecific.open_score}</td>
                            </tr>
                        </tbody>
                    </Table>

                    <p>This result is shown to you by processing your data through an Unsupervised Machine Learning model trained locally with GTX 1650. The data for training the model was taken from Kaggle at <a href="https://www.kaggle.com/tunguz/big-five-personality-test" target="_blank">BIG-FIVE-PERSONALITY-TEST</a>.</p>
                    <p>The model was serialized by a python library called "pickle" and then put into the django backend. </p> 
                </Container>
            </Jumbotron>
            
        </div>
    )
}

export default Results
