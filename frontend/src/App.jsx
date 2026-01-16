import React, { useEffect } from 'react'
import Home from './pages/home'

const App = () => {

    useEffect(() => {
        fetch("http://localhost:8000/").then((res) => res.json()).then(data => alert(data.message))
    }, [])

    return (
        <div>
            <Home />
        </div>
    )
}

export default App
