//[INSTALLING AND SET UP]

const express = require ('express'); 
const path = require('path'); 


const app = express(); 
const members = require('./Members'); // It's like our model


const logger = require('./middleware/logger'); 


//Init middleware. // this show like how a middleware works
app.use(logger); 

/*//this route
// gets all members
app.get('/api/members', (req, res) => {
    res.json(members); 
    //we don't have to do even JSON strigfy or anything
}); //*/

/*/get a single member 
app.get('/api/members/:id', (req,res) =>{

    const found = members.some(member => member.id  === parseInt(req.params.id)); 
    if(found) {
        res.json(members.filter(member => member.id === parseInt(req.params.id))); 
    }else {
        res.status(400).json({msg: `No Member with the id of ${req.params.id}` });
    }
})//*/

/*app.get('/', (req,res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html')); 
}); *///this isn't ideal becuz we have to put a route manually for every single page! contact..about.. etc!

// set static folder 
app.use(express.static(path.join(__dirname, 'public'))); //and now, all you have to do is put the files inside. that's it

app.use('/api/members', require('./routes/api/members')); 
// for most part is JSON Api to react with REACT

const PORT = process.env.port /* the server */ || 5000;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`)
}); 