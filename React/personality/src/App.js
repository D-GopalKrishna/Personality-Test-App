import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { useState, useEffect } from 'react'

import './App.css';
import Headers from './components/Headers';
import Results from './components/Results';
import IntroBlock from './components/IntroBlock';
import TestNameEnter from './components/TestNameEnter';
import ResultnameEnter from './components/ResultnameEnter';

import Test from './components/Test';





function App() {

  const [userData, setuserData] = useState([])

  const addUser = async (user) => {
    console.log(user.text)
    const userda = {
      "username": user.text,
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




  return (
    <Router>
      <Headers userData={userData} />

      <Route path='/' exact render={(props) => (
          <> 
            <IntroBlock />
          </>
        )} />

      <Route path='/entername' exact render={(props) => (
        <> 
          <TestNameEnter onAdd={addUser} userData={userData} />
        </>
      )} />

      <Route path='/resultentername' exact render={(props) => (
        <> 
          <ResultnameEnter userData={userData} />
        </>
      )} />


      <Route path='/test/*' exact render={(props) => (
        <> 
          <Test userData={userData} />
        </>
      )} />

      {/* <Route path='/results/*' component={Results} /> */}
      <Route path='/results/*' exact render={(props) => (
        <> 
          <Results userData={userData}/>
        </>
      )} />


    </Router>

  );
}

export default App;
