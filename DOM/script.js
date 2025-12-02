//This is just a script to try okay? 
// I love clean code. 

function execute() {
    //For the execution paragraph 
   const execution = document.getElementById("demo");
   execution.innerHTML = "It has executed! "; 

   let body = document.body; 
   let div = document.createElement("div"); 
   div.textContent='Hello there lol ! ';
   body.append(div); 

   body.remove()

}



const execute = ()=>{
    consoel.log('const fucntion')
}


/**
 * Promises
 * 
 * 1. Definition
 * 2. Call
 * 
 */


function execute1() {
    // For the execution paragraph 
   const execution= document.getElementById("demo");
   execution.innerHTML = "It has executed! ";
   
   // The actual DOM Traversal work 

   let grandparent = document.getElementById("grandparent-id");
   changeColor(grandparent);

   const parents =Array.from(document.getElementsByClassName("parent"));
   
   parents.forEach(element => {
       changeColor(element);
   });
    //    python  is just powerful when iterating through iterable
   
   parents.forEach(changeColor);
}

function changeColor(element){

    element.style.backgroundColor = "#333"
}


/*
    grandparent = document.querySelector(".grandparent")
    
    children = grandparent.querySelectorAll(".child")

   let childOne= document.querySelector("#child-one")
   
   changeColor(childOne);

   let childTwo = childOne.nextElementSibling
   changeColor(childTwo)
*/

