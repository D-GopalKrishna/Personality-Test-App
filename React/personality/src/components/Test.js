import React from 'react'
import { useState, useEffect } from 'react'
import {Link, useHistory} from 'react-router-dom';

import QuestionBlock from './QuestionBlock';
import {Jumbotron, Container} from 'react-bootstrap';
import './styling/Test.css';



const Test = () => {
    let history = useHistory();


    const [selected, setSelected] = useState([])
    

    // const [userQuestionsChoice, setuserQuestionsChoice] = useState([])

    const onClickSubmit = async () => {

    // const AdduserQuestionsChoice = async () => {


        console.log("Submit clicked")
        let hrefy = String(window.location.href).split('/')
        let hrefy_name = hrefy[hrefy.length - 1]
        console.log(hrefy[hrefy.length - 1])

        console.log("url_got")

        // selected = addSelected()

        // console.log(question.text)
        const userda = {
            "q1": selected[0].button_value,
            "q2": selected[1].button_value,
            "q3": selected[2].button_value,
            "q4": selected[3].button_value,
            "q5": selected[4].button_value,
            "q6": selected[5].button_value,
            "q7": selected[6].button_value,
            "q8": selected[7].button_value,
            "q9": selected[8].button_value,
            "q10": selected[9].button_value,
            "q11": selected[10].button_value,
            "q12": selected[11].button_value,
            "q13": selected[12].button_value,
            "q14": selected[13].button_value,
            "q15": selected[14].button_value,
            "q16": selected[15].button_value,
            "q17": selected[16].button_value,
            "q18": selected[17].button_value,
            "q19": selected[18].button_value,
            "q20": selected[19].button_value,
            "q21": selected[20].button_value,
            "q22": selected[21].button_value,
            "q23": selected[22].button_value,
            "q24": selected[23].button_value,
            "q25": selected[24].button_value,
            "q26": selected[25].button_value,
            "q27": selected[26].button_value,
            "q28": selected[27].button_value,
            "q29": selected[28].button_value,
            "q30": selected[29].button_value,
            "q31": selected[30].button_value,
            "q32": selected[31].button_value,
            "q33": selected[32].button_value,
            "q34": selected[33].button_value,
            "q35": selected[34].button_value,
            "q36": selected[35].button_value,
            "q37": selected[36].button_value,
            "q38": selected[37].button_value,
            "q39": selected[38].button_value,
            "q40": selected[39].button_value,
            "q41": selected[40].button_value,
            "q42": selected[41].button_value,
            "q43": selected[42].button_value,
            "q44": selected[43].button_value,
            "q45": selected[44].button_value,
            "q46": selected[45].button_value,
            "q47": selected[46].button_value,
            "q48": selected[47].button_value,
            "q49": selected[48].button_value,
            "q50": selected[49].button_value,
            "user": hrefy_name
        }
        
        console.log("userDa", userda)

        const res = await fetch(`http://127.0.0.1:8000/personality_api/userselection/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify(userda),
        })
        console.log("Submitted")


        history.push(`/results/${hrefy_name}`);

    //     const data = await res.json()
    //     console.log("hey data", data.url_key)

    //     setuserData([...userData, data])
    //     // console.log("hey setuserData", setuserData)  
    //     return data.url_key
    }

    





    const addSelected = async (select) => {
        // console.log(task)
    
        // const res = await fetch(`http://localhost:2200/tasks`, {
        //   method: 'POST',
        //   headers: {
        //     'Content-type': 'application/json',
        //   },
        //   body: JSON.stringify(task),
        // })
        // const data = await res.json()

        console.log(select)
        const data = select
    
        setSelected([...selected, data])
        console.log(selected)
        return selected

    }










    const [questions, setQuestions] = useState([])

    useEffect(() => {
        const getQuestions = async () => {
          const QuestionsFromServer = await fetchQuestions()
          setQuestions(QuestionsFromServer)
        }
        
        getQuestions()
    }, [])

    const fetchQuestions = async () => {
        const res = await fetch('http://127.0.0.1:8000/personality_api/question/')
        const data = await res.json()
    
        // console.log(data)
        return data
    }


    return (
        <div>
            <Jumbotron fluid>
                {/* <Container>
                    <Container>
                        <div style={{textAlign:'center'}}>
                            
                        </div>
                    
                    </Container>
                </Container> */}
                {/* <a href="#Niche">Bottom</a> */}
                {/* <form action=""> */}
                    <QuestionBlock questions={questions} addSelected={addSelected} />
                    <button onClick={onClickSubmit}>Submit</button>
                    {/* <input type="submit" className="SubmitText" value="Submit" /> */}
                {/* </form> */}
                {/* <p id="Niche"></p> */}
            </Jumbotron>
            
        </div>
    )
}

export default Test
