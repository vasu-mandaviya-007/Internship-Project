import React, { useEffect } from 'react'

const App = () => {

    useEffect(() => {
        fetch("http://localhost:8000/").then((res) => res.json()).then(data => alert(data.message))
    }, [])

    return (
        <div>
        </div>
    )
}

export default App
