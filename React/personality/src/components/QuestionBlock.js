import React from 'react';
import {Link} from 'react-router-dom';
import { useState, useEffect } from 'react'
import {Jumbotron, Container} from 'react-bootstrap';
import './styling/QuestionBlock.css';

// import './Header.css';


const QuestionBlock = ({questions, addSelected}) => {

    // const [QuesState, QuessetState] = useState({
    //     'input': '',
    // });
    // QuessetState(prevState => [...prevState, 'somedata'] );
    
    const [slec, setSlec] = useState('')

    let button_value;

    const onClick = (e) => {
        console.log('You clicked a button!')
        // console.log(e.target.value)
        // console.log(e.target.id)
        // console.log(e.target.name)
        // button_value = e.target.value
        // addSelected({button_value})
        let slecksss = [e.target.name,e.target.value]
        // console.log(slecksss)

        addSelected({slecksss})


        setSlec('')
    }


    return (
        <>
            {questions.map((question) => (

                <Container>
                    <Jumbotron>

                        <div className="QuestionsC">
                            <h5 className="QuestionsWritten" style={{textAlign:'center'}}>{question.question}</h5>
                            {/* <br/> */}
                            <div className="Option-list">
                                {/* <label className='labely' htmlFor="one">1</label> */}
                                <input className="Opt" type="radio" name={question.id} id="one" value="1" onClick={onClick} onChange={(e) => setSlec(e.target.value)}  />
                                <input className="Opt Opt2" type="radio" name={question.id} id="two" value="2" onClick={onClick} onChange={(e) => setSlec(e.target.value)} />
                                {/* <label htmlFor="two">2</label> */}
                                <input className="Opt Opt3" type="radio" name={question.id} id="three" value="3" onClick={onClick} onChange={(e) => setSlec(e.target.value)} />
                                {/* <label htmlFor="three">3</label> */}
                                <input className="Opt Opt2" type="radio" name={question.id} id="four" value="4" onClick={onClick} onChange={(e) => setSlec(e.target.value)} />
                                {/* <label htmlFor="four">4</label> */}
                                <input className="Opt" type="radio" name={question.id} id="five" value="5" onClick={onClick} onChange={(e) => setSlec(e.target.value)} />
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
