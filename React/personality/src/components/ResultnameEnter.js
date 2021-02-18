import React from 'react'
import {Link, useHistory} from 'react-router-dom';
import {Jumbotron, Container} from 'react-bootstrap';
import { useState, useEffect } from 'react'


const ResultnameEnter = ({userData}) => {


    let history = useHistory();

    const [text, setText] = useState('')
    const onClick = (e) => {
        // e.preventDefault()
        // if (!text) {
        //     alert('Please add your name!')
        //     return 
        // }
        // onAdd({text})

        console.log(userData[0])
        let user_urlkey = userData[0].url_key;
        setText('')
        history.push(`/results/${user_urlkey}`);

    }
    


    function handleSubmit(e) {
        e.preventDefault()
    }



    return (
        <div>
            <Jumbotron fluid className="jumboStyle">
                <Container>
                    <Container>
                        <div className="NameEnter">
                            <br/>
                            <br/>
                            <br/>
                            <h5>Enter your Name</h5>
                            <div className="NameEnter">
                                <input type="text" value={text} className="TextInput" onChange={(e) => setText(e.target.value)} />
                                <br/>
                                <br/>
                                <br/>

                                <div class="AnswerButton">
                                    <div>
                                        <p>Answer one by one</p>
                                        <Link onClick={onClick}><input type="button" className="SubmitText" value="Take Test" placeholder="Ex. Nik" /></Link>
                                        {/* <input type="submit" className="SubmitText" value="Take Test" placeholder="Ex. Nik" /> */}

                                    </div>
                                </div>
                            </div>
                        </div>
                    </Container>
                </Container>
            </Jumbotron>

        </div>
    )
}

export default ResultnameEnter
