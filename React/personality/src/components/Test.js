import React from 'react'
import { useState, useEffect } from 'react'

import QuestionBlock from './QuestionBlock';
import {Jumbotron, Container} from 'react-bootstrap';
import './styling/Test.css';



const Test = () => {


    const [userQuestionsChoice, setuserQuestionsChoice] = useState([])

    const addQuestionData = async (question) => {
        console.log(question.text)
        const userda = {
            "q1": "2",
            "q2": "3",
            "q3": "3",
            "q4": "3",
            "q5": "3",
            "q6": "2",
            "q7": "2",
            "q8": "1",
            "q9": "2",
            "q10": "1",
            "q11": "3",
            "q12": "1",
            "q13": "4",
            "q14": "3",
            "q15": "4",
            "q16": "4",
            "q17": "2",
            "q18": "2",
            "q19": "4",
            "q20": "1",
            "q21": "2",
            "q22": "2",
            "q23": "2",
            "q24": "1",
            "q25": "2",
            "q26": "2",
            "q27": "1",
            "q28": "2",
            "q29": "3",
            "q30": "4",
            "q31": "5",
            "q32": "2",
            "q33": "1",
            "q34": "4",
            "q35": "5",
            "q36": "4",
            "q37": "2",
            "q38": "5",
            "q39": "4",
            "q40": "2",
            "q41": "1",
            "q42": "3",
            "q43": "4",
            "q44": "5",
            "q45": "2",
            "q46": "5",
            "q47": "2",
            "q48": "3",
            "q49": "1",
            "q50": "4",
            "user": "1ba5801f-372c-4cc0-88f4-a471dbfa9f32"
        }

        const res = await fetch(`http://127.0.0.1:8000/personality_api/userdata/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify(userda),
        })
        const data = await res.json()
        console.log("hey data", data.url_key)

        setuserData([...userData, data])
        // console.log("hey setuserData", setuserData)  
        return data.url_key
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

                <QuestionBlock questions={questions} />

            </Jumbotron>
            
        </div>
    )
}

export default Test
