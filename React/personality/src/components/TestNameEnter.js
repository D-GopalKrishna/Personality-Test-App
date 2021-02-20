import React from 'react'
import {Link, useHistory} from 'react-router-dom';
import {Jumbotron, Container} from 'react-bootstrap';
import { useState, useEffect } from 'react'

import './styling/TestEnterName.css';



const TestNameEnter = ({onAdd, userData}) => {



    let history = useHistory();

    const [text, setText] = useState('')
    const onSubmit = (e) => {
        e.preventDefault()
        if (!text) {
            alert('Please add your name!')
            return 
        }

        let i, gotit;
        for (i in userData){
            if (userData[i].username==text){
                // let user_urlkey = userData[i].url_key;
                // history.push(`/results/${user_urlkey}`);
                gotit = 'Gotit';
            }
        }
        if (gotit=='Gotit'){
            alert('This name is already taken!')
            // pass
        }
        else{
            // alert('Please add a name that has taken the test!')
            // break
            onAdd({text})
            history.push(`/enteredname/${text}`);

            // console.log(userData[userData.length - 1])
            // let user_urlkey = userData[0].url_key;
        }


        
        
        setText('')

    }

    


    // function pushMan(e) {
        

    //     e.preventDefault()
    // }



    return (
        <div>
            <Jumbotron fluid className="jumboStyle">
                <Container>
                    <Container>
                        <form action="" onSubmit={onSubmit}>

                            <div className="NameEnter">
                                <br/>
                                <br/>
                                <br/>
                                <h5>Enter a unique username</h5>
                                <div className="NameEnter">
                                    <input type="text" value={text} className="TextInput" onChange={(e) => setText(e.target.value)} />
                                    <br/>
                                    <br/>

                                    <div class="AnswerButton">
                                        {/* <p>Answer one by one</p> */}
                                        {/* <Link to='/test'><input type="button" className="SubmitText" value="Take Test" placeholder="Ex. Nik" /></Link> */}
                                        <input type="submit" className="SubmitText" value="Submit" placeholder="Ex. Nik" />

                                        
                                    </div>
                                </div>
                            </div>
                        </form>

                        {/* <div>
                            <p>Get Results</p>
                            <Link to='/test'><input type="button" className="SubmitText" value="Take Test" placeholder="Ex. Nik" /></Link>
                            <input type="submit" className="SubmitText" value="Take Test" placeholder="Ex. Nik" />

                        </div> */}
                    </Container>
                </Container>
            </Jumbotron>
            
        </div>
    )
}

export default TestNameEnter