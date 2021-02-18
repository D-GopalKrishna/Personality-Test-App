import React from 'react';
import {Link} from 'react-router-dom';
import { useState, useEffect } from 'react'
import {Jumbotron, Container} from 'react-bootstrap';
import './styling/QuestionBlock.css';

// import './Header.css';


const QuestionBlock = ({questions}) => {

    // const [QuesState, QuessetState] = useState({
    //     'input': '',
    // });
    // QuessetState(prevState => [...prevState, 'somedata'] );


    const onClick = (e) => {
        console.log('You clicked a button!')
        console.log(e.target.value)
    }


    return (
        <>
            {questions.map((question) => (

                <Container>
                    <Jumbotron>

                        <div className="QuestionsC">
                            <h5 style={{textAlign:'center'}}>{question.question}</h5>
                            <br/><br/>
                            <div className="Option-list">
                                {/* <label className='labely' htmlFor="one">1</label> */}
                                <input className="Opt" type="radio" name={question.id} id="one" value="1" onClick={onClick}/>
                                <input className="Opt Opt2" type="radio" name={question.id} id="two" value="2" onClick={onClick}/>
                                {/* <label htmlFor="two">2</label> */}
                                <input className="Opt Opt3" type="radio" name={question.id} id="three" value="3" onClick={onClick}/>
                                {/* <label htmlFor="three">3</label> */}
                                <input className="Opt Opt2" type="radio" name={question.id} id="four" value="4" onClick={onClick}/>
                                {/* <label htmlFor="four">4</label> */}
                                <input className="Opt" type="radio" name={question.id} id="five" value="5" onClick={onClick}/>
                                {/* <label htmlFor="five">5</label> */}
                            </div>

                        </div>
                        
                    </Jumbotron>
                </Container>
            ))}
        </>
    )
}

export default QuestionBlock
