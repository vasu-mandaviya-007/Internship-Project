import React, { useEffect } from 'react'
import Home from './pages/home'

const App = () => {

    useEffect(() => {
        fetch("http://localhost:8000/").then((res) => res.json()).then(data => console.log(data))
    }, [])

    return (
        <div>
            <Home />
        </div>
    )
}

export default App
