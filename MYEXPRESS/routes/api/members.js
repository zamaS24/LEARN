const express = require('express'); 
const members = require('../../Members'); //This means that as if the members array is in this file. 

const router = express.Router(); 

//get all members 
router.get('/', (req, res) => {
    res.json(members); 
    members.forEach(member => console.log(`nom: ${member.name} email: ${member.email}`))
}) //  it is the route /api/members/  but we have sait it in the index when we use app.use(...)

//get single member 
router.get('/:id', (req, res) => {
    //connexion a la base de donnes..etc
    const found =  members.some(member => member.id === parseInt(req.params.id))
    
    if(found) {
        res.json(members.filter(member => member.id === parseInt(req.params.id)));
    }else {
        res.status(400).json({msg :`No person with the id of ${req.params.id}`})
    }
})




//create a member 
router.post('/', (req, res )=> {

    let newMember = {
        id: 123,
        name : req.body.name, 
        email: req.body.email,
        status: "active"
    }

    //if there isn't a newMember.name or there isn't an email. in the object. 
    //this is javascript power. 
    if(!newMember.name || !newMember.email)
    {
        return res.status(400).json({msg:'please include a name and email'});
    }
    
    members.push(newMember); 
    res.json(members); 
})


//UPDATE MEMBER
router.put('/:id', (req, res) => {
    //search the memebr
    const found =  members.some(member => member.id === parseInt(req.params.id))
    
    if(found) {
        const updMember = req.body; 
        members.forEach(member => {
            if (member.id === parseInt(req.params.id)){
                member.name = updMember.name ? updMember.name : member.name;  
                member.email = updMember.email ? updMember.email : member.email; 
                
                res.json({msg: 'Member updated', member});
            }
        })
    }else {
        res.status(400).json({msg :`No person with the id of ${req.params.id}`})
    }
})

//delete member 
router.delete('/:id', (req, res) => {
    const found =  members.some(member => member.id === parseInt(req.params.id))
    
    if(found) {
        res.json({ msg: "member deleted",members: members.filter(member => member.id !== parseInt(req.params.id))});
    }else {
        res.status(400).json({msg :`No person with the id of ${req.params.id}`})
    }
}) 
 



module.exports = router; 