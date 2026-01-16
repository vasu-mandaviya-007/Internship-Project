import React, { useEffect } from 'react'
import Home from './pages/home'

const App = () => {

    useEffect(() => {
        fetch("http://localhost:8000/").then((res) => res.json()).then(data => alert(data.message))
    }, [])

    return (
        <div>
<<<<<<< HEAD
            <Home />
=======
>>>>>>> 2234c0fdadbc139cc641dda609db31186d14da9b
        </div>
    )
}

export default App
