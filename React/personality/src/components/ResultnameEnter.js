import React from 'react'
import {Link, useHistory} from 'react-router-dom';
import {Jumbotron, Container} from 'react-bootstrap';
import { useState, useEffect } from 'react'


const ResultnameEnter = ({userData}) => {


    let history = useHistory();

    const [name, setName] = useState('')
    const onClick = (e) => {

        if (!name) {
            alert('Please add your name!')
            return 
        }
        // e.preventDefault()
        // if (!text) {
        //     alert('Please add your name!')
        //     return 
        // }
        // onAdd({text})

        let i, gotit;

        for (i in userData){
            if (userData[i].username==name){

                let user_urlkey = userData[i].url_key;
                history.push(`/results/${user_urlkey}`);
                gotit = 'Gotit';
            }
        }
        
        if (gotit=='Gotit'){
            // pass
        }
        else{
            alert('Please add a name that has taken the test!')
            // break
        }

        console.log(name)
        // console.log(userData)
        // let user_urlkey = userData[0].url_key;
        setName('')
        // history.push(`/results/${user_urlkey}`);

    }
    // setText([...text, text])

    


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
                                <input type="text" value={name} className="TextInput" onChange={(e) => setName(e.target.value)} />
                                <br/>
                                <br/>

                                <div class="AnswerButton">
                                    <div>
                                        <Link onClick={onClick}><input type="button" className="SubmitText" value="Get Results" placeholder="Ex. Nik" /></Link>
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
