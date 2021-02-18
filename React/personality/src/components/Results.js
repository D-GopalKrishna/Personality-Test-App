import React from 'react'
import {Link} from 'react-router-dom'
import {Jumbotron, Container, Table} from 'react-bootstrap';
import './styling/Results.css';


const Results = ({useData}) => {














    return (
        <div>
            <Jumbotron className="jumboStyle">
                <Container>
                    <h5>Hello! {}</h5>
                    <p>According to the ML model your data was passed through, you come under Personality type - {0}. All the metrics are out of 10. </p>
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
                                <td>Otto</td>
                            </tr>
                            <tr>
                                <td>Neurotic</td>
                                <td>Thornton</td>
                            </tr>
                            <tr>
                                <td>Agreeable</td>
                                <td>Thornton</td>
                            </tr>
                            <tr>
                                <td>Conscientious</td>
                                <td>Thornton</td>
                            </tr>
                            <tr>
                                <td>Open</td>
                                <td>Thornton</td>
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
