function addNums (a,b) {
    return a + b ; 
}   

//module.exports = addNums; 
// or you can 
export {addNums}
//export {addNums}
//and then in the server.js we make : 
// import {addNums} from './addNums' but ranme addNums to mjs
//Also the server.js to server.mjs
//Also in execution it must be node server.mjs


//The other option is to alter the package.json 
// (keeping track with node modules and your project information)
