import React from 'react'
import { useState, useEffect } from 'react'
import {Link, useHistory} from 'react-router-dom';

import QuestionBlock from './QuestionBlock';
import {Jumbotron, Container} from 'react-bootstrap';
import './styling/Test.css';



const Test = () => {
    let history = useHistory();


    const [selected, setSelected] = useState([])

    console.log("Selected ", selected)

    let i;
    let array_index = []
    let array_data = []
    for (i in selected){
        console.log(selected[i].slecksss)
        console.log("hi", selected[i].slecksss[0])
        if (selected[i].slecksss[0] in array_index) {
            //pass
            console.log("Already selected")

        }
        else{
            console.log("Pushed because it wasn't there already")
            array_data.push(selected[i].slecksss[1])
            array_index.push(selected[i].slecksss[0])

        }
    }

    console.log("Array data", array_data)
    console.log("Array index", array_index)


    // console.log(selected[1].slecksss[0] in array_data)
    // console.log(selected[1])













    

    // const [userQuestionsChoice, setuserQuestionsChoice] = useState([])

    const onClickSubmit = async () => {

    // const AdduserQuestionsChoice = async () => {
        if (49 < array_data.length < 52){                   // This is because its soemtimes adding one more elemenet extra.. Something with javascript
            console.log("Submit clicked")
            let hrefy = String(window.location.href).split('/')
            let hrefy_name = hrefy[hrefy.length - 1]
            console.log(hrefy[hrefy.length - 1])

            console.log("url_got")

            // selected = addSelected()

            // console.log(question.text)
            const userda = {
                "q1": array_data[0],
                "q2": array_data[1], 
                "q3": array_data[2],
                "q4": array_data[3],
                "q5": array_data[4],
                "q6": array_data[5],
                "q7": array_data[6],
                "q8": array_data[7],
                "q9": array_data[8],
                "q10": array_data[9],
                "q11": array_data[10],
                "q12": array_data[11],
                "q13": array_data[12],
                "q14": array_data[13],
                "q15": array_data[14],
                "q16": array_data[15],
                "q17": array_data[16],
                "q18": array_data[17],
                "q19": array_data[18],
                "q20": array_data[19],
                "q21": array_data[20],
                "q22": array_data[21],
                "q23": array_data[22],
                "q24": array_data[23],
                "q25": array_data[24],
                "q26": array_data[25],
                "q27": array_data[26],
                "q28": array_data[27],
                "q29": array_data[28],
                "q30": array_data[29],
                "q31": array_data[30],
                "q32": array_data[31],
                "q33": array_data[32],
                "q34": array_data[33],
                "q35": array_data[34],
                "q36": array_data[35],
                "q37": array_data[36],
                "q38": array_data[37],
                "q39": array_data[38],
                "q40": array_data[39],
                "q41": array_data[40],
                "q42": array_data[41],
                "q43": array_data[42],
                "q44": array_data[43],
                "q45": array_data[44],
                "q46": array_data[45],
                "q47": array_data[46],
                "q48": array_data[47],
                "q49": array_data[48],
                "q50": array_data[49],
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
        }
        
        else{
            alert('Fill the whole data!')
        }


        

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
                    <div className="DivTestSubmitBtn">
                        <button className="TestSubmitBtn" onClick={onClickSubmit}>Submit</button>
                    </div>
                    {/* <input type="submit" className="SubmitText" value="Submit" /> */}
                {/* </form> */}
                {/* <p id="Niche"></p> */}
            </Jumbotron>
            
        </div>
    )
}

export default Test
