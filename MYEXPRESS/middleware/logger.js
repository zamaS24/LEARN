const myMembers = require('../Members');

let myMiddlWare = function (req, res, next) {
    console.log(``); 
    next();
}


let anotherMiddlWare = function(req,res,next) {
    console.log("This is just another middleWare okay ? "); 
    next(); 
}
module.exports = myMiddlWare; 
module.exports = anotherMiddlWare; 