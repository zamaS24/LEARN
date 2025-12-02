const express = require('express'); 
const path = require('path'); 
const app = express();  
const myMiddlWare = require('./middleware/logger'); 

//body parser middleware
app.use(express.json())
app.use(express.urlencoded({extended:false}))

/*
    Your app will be here only like this: 
    app.use(); 
    app.use(); 
    app.use();  ..;etc
*/
//static folder
app.use( express.static(path.join(__dirname, 'public')))



//Middleware
//app.use(myMiddlWare); 

//Members API ROUTES

app.use('/try/members', require('./routes/api/members')); 

// You create your routes using the Router class. and then you make all of the links there
// and then here you will just specify which path will proceed that path. 
// the first path as you see has nothing to do with the hierarchy of the folder


//const memberRouters = require('./routes/api/members'); 
//app.use('/api/members', memberRouters);

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
})

app.get('/about', (req,res) => {
    res.json({msg:"this is a json response"})
})

//l'ecahnge de donnees sous format json. 
app.get('/users/:userId/books/:bookId', (req, res, next) => {
    console.log('It is handeling it before the response '); 
    next();
}, (req, res) => {
    
    res.send(req.params)
    //this to handle route. 
})

const PORT = process.env.port /* the server */ || 5000;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`)
}); 