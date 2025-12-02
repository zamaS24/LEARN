import express from 'express'

const app = express(); 


app.use(express.json())
app.use(express.urlencoded({extended:false}))


// get www.site.com/
app.get('/', (req, res) => {
    res.send('Home page'); 
})

const accidents = [
    {
        id:2020000001,
        nom:"Hamza OMARI",
        prenom:"Date S"
    }
]



app.get('/users', getAllUsers);



const PORT =  5000;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`)
});



