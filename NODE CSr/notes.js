/*
    [INTRO] [INSTALL]
    - Run js on the server. 
    - Node built on top of chrome v8 engine
    - JS on the browser we have the DOM but in node JS there is no document 
     or elements. 
    - There is no window object too. 
    
    [BASIC HELLO WORLD EXEMPLE]
    - See the  server.js file 
    - Execute the server.js and congrats you have executed your first web server
    - Ctrl + C to stop it. 

    [GLOBAL PROPERTIES]
    - __filename : path to file  
    - __dirname  : path to directory 

    [FILE SYSTEM MODULES/ Reading files]
    - We need to import the fs module from node
    - Start by reading a file. make a hi.txt file first. 
    - Execute the code on how to read file 
    - Noticing the asynchronous nature of nodeJS
    - readFile('hi.txt', (err,data) => { 

    [FILE SYSTEM MODULES / Writing to files/deleting files]
    - writeFile('hi.txt',newContent, {flag:"a"} ,(err)=>{
    - need to see the code

    [MODULES EXPORT AND IMPORT ]
    - require(./"<nameFile>");
    - module.export

    -(1) export {addNums}  works with import {addNums} from "./addNums.mjs" (use this better)
    - module.exports = addNums; works with const addNums = require('./addNums'); 
    - npm init -y  generate the package.json file
    - you have to rename the main attribute if it's not your main file. 
    - add "type": module (it will knows we use es6 modules) so we will use 
     (1) without renaming to mjs but just addNums.js
    -wen using ES modules in node we no longer have access to require, exports
     module.exports, __filename or __dirname
     so you can see thsese common js. 
    - In this tutorial we will continue using those module.exports...etc

    [BASIC HTML CONTENT]
    - http module and create the web server
    - execute that classic code to run the server
    - remove the "type": "module" from package.json as we said we will use 
    the require export
    - basically read the code in this part. 

    [[BASIC WEB SERVER ROUTING]]
    -Read the code, it's documented. 

    -!! If there is many pages, create teh view folder and put everything there

    [REDIRECTION]
    - Whenever the url is not valid redirct him to homepage ? 


    [NPM : NODE PACKAGE MANAGER]
    - included with node, a package manager called npm 
    - npm init (without the -y like seen previously)

    [NODE MON]
    - a package that will make our lifes so much easier. 
    - npm i -g nodemon (i for install and g for global that will install nodemon globaly on our computer)
    - (execute this command) we prefer to set it as a dev dependency for the package
      so we say : npm i -D nodemon(D for dev dependency)
      
    - we prefer to set it as a dev deependency in case of another person doesnt have it
     globally. 
    
    - we will have the node modules folder

    -gitignore file 
    -node_modules (in the gitignore file) so when we download the project from github 
      it will ignore the node modules folder. 
    - we can easily install thazt folder node_modules by the command
     -npm i 
    - now in the package.json delete the "test" or "build" property and replace it 
      with : "dev" :"nodemon server" so nodemon is the node monitor server
      any time we make any changes to any file it will automatically reload the server for us
    - make sure to verify that "start" : "node serve"

    -now instead of running the server with node server we can use
    - npm run dev
    - Now each time we make a change the server will be restarted

    -in development you'll want to run the "dev" script
    - and then on the sever you well run "start"

    [LEARN GIT codeStackr]
    [BASIC COMMANDS]

    git init        : initialize new git repo
    git add <file>  : add files to staging area
    git status      : check status of working tree
    git commit      : commit changes in staging area 
    git push        : Push to remote repo
    git pull        : pull latest from remote repo
    git clone       : clone remote repo locally
    git branch <branch name> : create a new branch
    ...etc


    -create folder
    -right click the folder, git-bash here
    - touch index.html
    - touch app.js
    -git init it will create a hidden file .git
    - git config --global user.name 'nomtuveux'
    - git config --global user.email 'nomtuveux'
    - git status
    - git add index.html
    - git rm --cached index.html
    - git add *.html (will add every html file)
    - git add git . (adds them all)
    - git reset (to undo the add . before the commit)
    
    -Now make change to H TML file
    - git status (youll see it says modified)
    - now alse git add . (now you'll see th files are ready to the staging area)
    - now commit the changes git commit (this is not working to me nicely idk )
    - use the git commit -m "your commit message"
    - Enter the message of why did you do: example: added new paragraph
    - open the jsfile and make some changes
    - git log (shows the hitory of commits and messages) (dispolay with enter and quit with q)
    - git ckeckout <commit_id> (commit id just few characters) (to return at some point)
    - you will notice that the code is gone because it was before the commit


    -git checkout master (we can see now the code in app js is back, we're ,pw p, the lmatest version)
    -git log         

    select git bash in terminal

    -what if we have a file or a folder that we don't want git to look out in your versiono control
    - add a .gitignore file 
    - touch .gitignore 
    - create log.txt : touch log.txt
    - mettre dans gitignore file : log.txt

    -now in git status you will see that it doesn't show the log.txt file. 
    (it works also with the folder (directory)) 
    (14eme minute)

    [DEPLOY TO HEROKU]









*/

const { rejects } = require("assert");

// [PROGRAM]

function faireEtap1(init,callback){
    return init + callback(); 
}


function anotherDisplay(arg)
{
    console.log("Another dispaley" + arg); 
}

function display(arg1, arg2)
{
    console.log(arg1+arg2); 
}

let myPromise = new Promise((resolve, reject) => {

    //traitement 
    let x = 0; 
    //condition

    //definir le succes
    if(x == 0){ 
        resolve("First","second"); 
    }
    else //definir l'echec
        reject("Reject"); 

}); 

//Calling the promise right? 
// en execution 
myPromise.then(
    (value, value2) => { //cas de succes
        console.log("oui c'est le cas de succès x a bien obtenu le zéro "); 
        display(value,value2); 
        anotherDisplay(value2); 
            
    }, (error) => {// cas de echec 
        display(error); 
    }
)//*/

let maPromesse = new Promise((resolve, reject) =>{
    let x = 0; 
    if(x == 0){
        resolve("succes"); 
    }else{
        reject("Echcec"); 
    }
})






// Expert Vision et NLP 
