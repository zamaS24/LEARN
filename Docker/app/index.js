// const app = require('express')(); 
const express = require('express'); 
const app = express() 




app.get('/humans/api', (req, res, next) => {
    res.json('Response from the server')
})


app.get('/', (req, res) => {
    res.json(
        {message: 'Docker is good! '}
    )
})



const port = process.env.PORT || 8080; 


app.listen(port, ()=> console.log(`App listening on port ${port}`))





