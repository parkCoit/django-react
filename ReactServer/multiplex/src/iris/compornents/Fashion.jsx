import { useState } from "react"
import "uat/style/Login.css"
import {fashion} from 'iris/api'

const Fashion = () =>{

    const [inputs, setInputs] = useState({})
    const {testNum} = inputs

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {testNum}
        alert(`정보 : ${JSON.stringify(request)}`)
        fashion(request)
        .then((response) => {
            console.log(`response is ${response.data.result}`)
            localStorage.setItem('token', JSON.stringify(response.data.result))
            alert(`정보 : ${JSON.stringify(response.data.result)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('에러')
        })
    }

    return(<>
        testNum : <input type="text" name="testNum" onChange={onChange} /><br/>
        <button onClick={onClick}> fashion </button>
    </>)
}

export default Fashion