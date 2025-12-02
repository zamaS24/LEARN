/* //[INSTALL - BASIC HELLO WORLD - GLOBAL PROPERTIES]
const http = require("http"); 
const HOSTNAME = process.env.HOSTNAME || "localhost"; 
const PORT = process.env.PORT || 3000;

//create the http server 
const server = http.createServer((req, response) =>{
    response.statusCode = 200;
    response.setHeader("content-type", "text/plain"); 
    response.end("hello world"); 
});

console.log(__filename); 
console.log(__dirname); 


server.listen(PORT, HOSTNAME, () =>{
    console.log(`server running at http://${HOSTNAME}:${PORT}`);

}) //*/



 /*/ [FILE SYSTEM MODULES / Reading files]=========================================
 // const {readFile , readFileSync } = require('fs'); 
 // and then remove fs genre: readFileSync('hi.txt',...etc)
 const fs = require('fs'); 
 try {
    fs.readFile('hi.txt', (err,data) => {
        //readFileSync : is the synchronous version 
        if (err) {
            console.error(err); 
            return; 
        }
        console.log(data.toString()); 
    })
 } catch(err) {
     console.error(err); 
 }

 console.log("log from outside"); 
 // This code will display : log from outside before the file. 
 // becuz of the asynchrounous nature of javascript. 
 //*/



/*/ [FILE SYSTEM MODULES / Writing to files] =======================================
const {writeFile, writeFileSync} = require("fs");
// const {appendFile}. on peut le faire comme ça seule.  

const newContent = "this is some new text"; 
writeFile('hi.txt',newContent, {flag:"a"} ,(err)=>{
    if (err){
        console.error(err); 
        return; 
    }
    console.log("Content written!"); 
}) 
//*/ 

// [FILE SYSTEM MODULES / renaming and deleting files] =======================================

/*/To rename
const {rename} = require ("fs"); 
rename ("hi.txt", "renamed.txt", (err) => {
    if (err) {
        console.error(err); 
        return; 
    }
    console.log("File renamed!"); 
});

// To delete
const {unlink } = require("fs"); 
unlink("renamed.txt", (err) => {
    if(err) {
        console.log(err);
    }
    console.log("File deleted"); 
}); 
//*/

/*/ [MODULES EXPORT AND IMPORT ] ==================================================
 import {addNums} from "./addNums.js"
//const addNums = require('./addNums'); 
const sum = addNums(2,2);

console.log(sum); 
//*/

/*/ [BASIC HTML CONTENT]============================================================

const http = require("http"); 

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.statuscode = 200;
    res.setHeader('Content-type', 'text/html');
    //res.write('hello world'); 
    //res.write('hello world again'); // we can write again and again 
    res.end("<h1> hello world </h1> "); 
}).listen(PORT, () => console.log(`Server is listening on port ${PORT}`));

//*/


/*/ [BASIC WEB SERVER WITH HTML FILES ]============================================ 
const http = require("http"); 
const fs = require("fs"); 
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.statuscode = 200;
    res.setHeader('Content-type', 'text/html');
    //res.write('hello world'); 
    //res.write('hello world again'); // we can write again and again 
    //res.end("<h1> hello world </h1> "); 
    fs.readFile("./index.html", (err, data) => {
        if(err) {
            console.error(err); 
            res.end(); 
        }else {
            res.write(data);  //
            res.end();        // Or res.end(data); 
        }

    })
}).listen(PORT, () => console.log(`Server is listening on port ${PORT}`));

//*/

//(we can see now the code in app js is back, we're ,pw p, the lmatest version)/[BASIC WEB SERVER ROUTING]======================================================
// we want to route certain files to certain urls
// when we use the lcolahost:3000 we still getting the same page
const http = require("http"); 
const fs = require("fs"); 
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {

    res.statuscode = 200;
    res.setHeader('Content-type', 'text/html');
    console.log(req.url, req.method); 

    //when refreshing we get this: 
    // / GET 

    let path ='./'; 

    switch(req.url){
        case '/' : 
            path += "index.html"; 
            res.statusCode = 200;
            break; 

        case '/about': 
            path += "/about.html"; 
            res.statusCode = 200;
            break; 
        default: 
        path+='/404.html';
        res.setHeader('Location', '/'); 
        res.statusCode = 301;
        break; 
    }
    fs.readFile(path, (err, data) => {
        if(err) {
            console.error(err); 
            res.end(); 
        }else {
            res.write(data);  //
            res.end();        // Or res.end(data); 
        }

    })
}).listen(PORT, () => console.log(`Server is listening on port ${PORT}`));

//*/// [ Redirect ]
// we want to send them to the home page whenever the url is not valid
// we but these lines of code here : 















