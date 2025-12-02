const moment = require('moment'); 

const logger = (req, res, next) => {
    console.log(`${req.protocol}://${req.get('host')}${req.originalUrl} : ${moment().format()}`); 
    //console.log('yup it works!'); 
    next(); 
}

module.exports = logger; 