const express = require('express'); 
const path = require('path'); 
const neo4j = require('neo4j-driver'); 




var app = express(); 
//body parser middleware
app.use(express.json())
app.use(express.urlencoded({extended:false}))

const config = {
    "neo4j": {
      "url": "bolt://127.0.0.1:11003",
      "authUser": "neo4j",
      "authKey": "password"
    }
  }

  const driver = neo4j.driver(
    config.neo4j.url,
    neo4j.auth.basic(config.neo4j.authUser, config.neo4j.authKey)
  );

  
  const session = driver.session();
//Routes
app.post('/', (req,res) => {
    res.send('Home page'); 
})

async function getUserByName(name) {
    await session.readTransaction(tx =>{
    return tx.run(
        `match(u:USAGER) return u where u.name = ${name}`
    )
    })

}



async function createUser(name) {
    session = driver.session({
        defaultAccessMode: session.WRITE,
        database: 'neo4j'
    }); 
    await session.writeTransaction(tx => {
        return tx.run(
            'create (person:PERSON(name:$name}) return p', {name} 
        )
    })
}





app.get('/:name', (req,res) => {
    
    console.log('\n It starts here! ')
    const name = req.params.name; 

    
    session
        .run(`match(u:USAGER) return u`)
        .then(function(result) {
            console.log(result); 
            /*result.records.forEach(function(record) {
                console.log(record._fields[0].properties); 
            })*/
        })
        .catch(function(err){
            console.log('this is the error :' + err);
        }) 
    res.send('It works!!' +`<h1> oui </h1>`); 
})


//Listening
const PORT = process.env.port /* the server */ || 5000;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`)
}); 
