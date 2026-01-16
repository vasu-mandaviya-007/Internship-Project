import React, { useEffect } from 'react'

const App = () => {

    useEffect(() => {
        fetch("http://localhost:8000/").then((res) => res.json()).then(data => console.log(data))
    }, [])

    return (
        <div>

        </div>
    )
}

export default App
