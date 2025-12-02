# Notes of javascript
> ## Tables of contents
> * [Extra](#extra)
> * [Let var const](#let-var-const)
> * [Objects](#objects)



<br>

# Extra 
* __infinity__ is a number: typeof Infinity returns number.
division / 0 returns infinity   
* `number.MAX_VALUE`  
* `number.EPSILON` 
* __===__ is equal value and equal type 
* __condition ternary operator__
    ```js
    let voteable = (age < 18) ? "Too young":"Old enough";
    ```
* __nullish operator__ ?? returns the first argument if it is not nullish (null or undefined).
    ```js
    let name = null;
    let text = "missing";
    let result = name ?? text;
    ```
* __for in loops__ over properties of an object or array, but in array it's the index that is being itrated

* __for of__, iterates over the elements of an array, or any iterable

* __Try catch and errors__
    ```js
    let num = 1;
    try {
    num.toUpperCase();   // You cannot convert a number to upper case
    }
    catch(err) {
    document.getElementById("demo").innerHTML = err.name;
    }
    finally(){
        //code executing regardless of the try catch blocks
    }
    ```
    __The throw statement allows you to create a custom error.__
    ```js
        throw "Too big";    // throw a text
        throw 500;          // throw a number
    ```



<br>  

# let var const

* __const__ 
    * is for constants
    * It does not define a constant value. It defines a constant reference to a value. you can create a constant array and change it's elements

* __let__
    * let is generally preferred in modern JavaScript coding because it provides better scoping and helps prevent common programming mistakes. 
    * cannot be redeclared
    * have block scope
    * can be redeclared in a different block scope 
    

* __var__
    * Use var when you intentionally want a variable to have function scope and want to take advantage of hoisting (though this is not recommended for most cases).
    * can be redeclared

__Example code__
```js
function example() {
    if (true) {
        var varVariable = "I am a var variable";
        let letVariable = "I am a let variable";
    }
    console.log(varVariable); // Outputs: "I am a var variable"
    console.log(letVariable); // Throws ReferenceError
}
```

<br> 

# Objects
__example__
```js
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
```
## accessing the object properties
    objectName.propertyName
or  

    objectName["propertyName"]

__this__ : refers to the object   
__objects can have methods stored in property__
```js
    const person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,

  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

# JS events
*comon HTML events*

|Event| Description|
|:--|:--|
| onchange | An HTML element has been changed |
| onclick | The user clicks an HTML element |
| onmouseover | The user moves the mouse over an HTML element |
| onmouseout | The user moves the mouse away from an HTML element |
| onkeydown | The user pushes a keyboard key |
| onload | The browser has finished loading the page |

__example__
```html
<button onclick="myFucntion()"> click me </button>
```

<br>

# JS Strings
... check reference

## template literals
* Variable substitution
    ```js
    let text = `Welcome ${firstName}, ${lastName}!`;
    ```
* HTML templates
    ```js
    let header = "Templates Literals";
    let tags = ["template literals", "javascript", "es6"];

    let html = `<h2>${header}</h2><ul>`;
    for (const x of tags) {
    html += `<li>${x}</li>`;
    }
    html += `</ul>`;
    ```



__variable substitutions__
```js
let firstName = "John";
let lastName = "Doe";

let text = `Welcome ${firstName}, ${lastName}!`;
```

<br> 

# JS arrays
 * ## array methods
```js
const fruits = ["Banana", "Orange", "Apple", "Mango"];

// get length 
let size = fruits.length;

// convert all elements to string 
let stringArray = array.toString()

// join method and specify separator
fruits.join(" * ");

// pop and push 
let fruit = fruits.pop()
fruis.push("kiwi")

// delete ,  leaves undefined holes in the array.
delete fruits[0] 

// concat (merging) two arrays, works also for string
const myGirls = ["Cecilie", "Lone"];
const myBoys = ["Emil", "Tobias", "Linus"];
const myChildren = myGirls.concat(myBoys);

// flattening an array
const flat = myArr.flat()

// slicing an array, it creates a new array
const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1, 3);
```

* ## Array sort
    About the __sort()__ meethod.
    When the sort() function compares two values, it sends the values to the compare function, and sorts the values according to the returned (negative, zero, positive) value. 

    * If the result is negative, a is sorted before b. 

    * If the result is positive, b is sorted before a. 

    * If the result is 0, no changes are done with the sort order of the two values.
    ```js
    // reversing an array 
    fruits.reverse();

    // sorting an array, it works alphabetically
    fruits.sort();

    // by default the sort() function sorts values as strings, so dealing with numbers it won't work. and we need to pass a sorting function

    const points = [40, 100, 1, 5, 25, 10];
    points.sort(function(a, b){return b - a});

    // sorting in random order
    points.sort(function(){return 0.5 - Math.random()});

    ```
* ## Sorting object arrays

    ```js
    const cars = [
    {type:"Volvo", year:2016},
    {type:"Saab", year:2001},
    {type:"BMW", year:2010}
    ];
    cars.sort(function(a, b){return a.year - b.year});
    ```
<br>

* ## Array iteration

    ```js
    const numbers = [45, 4, 9, 16, 25];
    numbers.forEach((value, index, array)=>{
        // code here

    });
    // index and array are optional parameters, and @param array represents the whole array
    ```

* ## Array map, filter, reduce, every, some, indexof  
    

    ```js
    // map : Associate for each value another value --> anotherThing
    const numbers1 = [45, 4, 9, 16, 25];
    const numbers2 = numbers1.map(myFunction);
    function myFunction(value, index, array) {
    return value * 2;
    }

    // flatmaps create a new array by flatenning the array
    const myArr = [1, 2, 3, 4, 5, 6];
    const newArr = myArr.flatMap((x) => x * 2);

    // filtering an array (elements that pass a condition)
    const numbers = [45, 4, 9, 16, 25];
    const over18 = numbers.filter(myFunction);
    function myFunction(value, index, array) {
    return value > 18;
    }

    // reduce, like applying a function and return a single value example: sum of numbers
    const numbers = [45, 4, 9, 16, 25];
    // it can accept an initial value here is 100
    let sum = numbers.reduce(myFunction, 100); 
    // value, index, array are optional
    function myFunction(total, value, index, array) {
    return total + value;
    }
        
    // some, checks if an array value, passes some 
    let someOver18 = numbers.some(myFunction);
    function myFunction(value, index, array) {
    return value > 18;
    }


    // index of returns position
    array.indexOf(item, start) // start is optional

    
    ```
    * Arrays can be const meaning that the variable can't be reassigned : 
        ```js  
        const array = [1,2,3]
        ```

<br>

# JS dates
there is 9 ways to create dates ni JS as follow
```js
new Date()
new Date(date string)

new Date(year,month)
new Date(year,month,day)
new Date(year,month,day,hours)
new Date(year,month,day,hours,minutes)
new Date(year,month,day,hours,minutes,seconds)
new Date(year,month,day,hours,minutes,seconds,ms)

new Date(milliseconds)
```
Examples 
```js 
const d = new Date("October 13, 2014 11:13:00");
const d = new Date("2022-03-25");
const d = new Date(2018, 11, 24, 10, 33, 30, 0);
```

__*NB* : JS COUNTS MONTHS FROM 0 TO 11__

## Displaying dates
Use the `toString()` method
or 
```js
d = new Date()
d.toString()
d.toDateStrinig()
```
using Standards 
```js
// UTC standard 
d.toUTCString();

//  ISO standard
d.toISOString();
```
<br>

# BOOLEAN
* ### everything witha value is true
* ### everything without a value is false*
* ### true and false values

<br>

#  Promises
Promises in JavaScript are a way to handle asynchronous operations in a more organized and manageable manner. Asynchronous operations are tasks that may take some time to complete, such as fetching data from a server, reading a file, or waiting for a timer to expire. Promises provide a way to work with these operations, making your code more readable and maintainable. 

Promises in JavaScript are a way to handle asynchronous operations in a more organized and manageable manner. Asynchronous operations are tasks that may take some time to complete, such as fetching data from a server, reading a file, or waiting for a timer to expire. Promises provide a way to work with these operations, making your code more readable and maintainable.

A Promise represents a value that may not be available yet but will be at some point in the future. It has three states:

- Pending: Initial state, before the promise is fulfilled or rejected. 
- Fulfilled (Resolved): The operation completed successfully, and the promise now has a resulting value. 
- Rejected: The operation encountered an error, and the promise now has a reason for failure.

```js
const myPromise = new Promise((resolve, reject) => {
  // Asynchronous operation (e.g., fetching data)
  // If successful, call 'resolve' with the result
  // If an error occurs, call 'reject' with an error message
});

```
```js
const fetchData = new Promise((resolve, reject) => {
  setTimeout(() => {
    const data = { message: 'Data fetched successfully' };
    // Simulate a successful operation
    resolve(data);
    // If an error occurs, you would call reject with an error message
    // reject("Failed to fetch data");
  }, 2000); // Simulate a 2-second delay
});

// Consuming the promise
fetchData
  .then((result) => {
    console.log(result); // This will be called when the promise is resolved
  })
  .catch((error) => {
    console.error(error); // This will be called if the promise is rejected
  });


```
I feel like I should always see promises as just some block of code that has to be run in the background, until it's resolved or reject based on defined cases in the promise. 
And we are talking just about definition. Because the actual call should be done when we are calling 
.then(returnedResolve) .catch(returnedError) 

the (resolve, reject) => {} arrow function, is us implementing the callback function calls without us knowing it.when we call resolve() or reject()

very high level stuff



* the promise also is executed immediately when we create the promise

the .then() and .catch() are like methods used dependenlty with the state of the promise

__! be careful that the promise itself has one of the three states mentioned above__ 

> ### about then()
> The promise is resolved, but the resolution callback (the one inside .then()) is not executed immediately. Instead, it's placed in the microtask queue.

>  ### promise chain
> It's when we have a promise inside a then(), we  should return it and make another .then()

## Additional stuff about promises very important
- in the `.then()` statement, we pass a callback with the resolved parameter, and if it returns another promise. we can process it by chaining another .then()
we can add another .then() even if the previous doesn't return a promise

- also what is in the then() in js will be executed in a micro task. after the next sequentiel code, but for example when there's another async operation like in/out, then that microtask will be exectued like in multiprogramming os concept
<br>

- the whats inside the promise() is executed directly, but when it occurs any async operation like in/out or reading from server, the nature of non bloking in js will continue to run to what's next. __(to be corrected if not true):__ that's why in some function when we use promise and the next code depends on the output of this promise, well in this nature of non bloking it will continue to execute but using await will tell it no you should wait here and just execture what's in next of the function until that this promise is resolved so that we will return and continue after the await.  



<br>

# Async await
When we work with promises, or the asyncronous functions, and we want
to wait for something before jummping in to the next lines of code due to the nature of asynchronous stuff. then the need of await is crucial.  
***Example***
```js
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
  } catch (error) {
    // Handle errors here
    console.error(error);
  }
}
```

<br>

# Object property shorthand

when the name of the attribute of the object is also the same of the name of the variable, so we don't need to do 
obj{
    varname:varname
}
the example above explains it 
```js
// Without object property shorthand
const firstName = 'John';
const lastName = 'Doe';

const person = {
  firstName: firstName,
  lastName: lastName
};

// With object property shorthand
const firstName = 'John';
const lastName = 'Doe';

const person = {
  firstName,
  lastName
};


// also 
// Using traditional object property assignment
const personWithComputedProperty = {
  name,
  'currentAge': age + 5 // Property name is different, and value is computed
};
```

<br>  

# Destructuring
**! A rest element must be last in a destructuring pattern.**

* ## Array destructuring 
  ```js
  const [element1, element2, ...rest] = myArray;
  ```

* ## Object destructuring 
  ```js
  const { property1, property2 } = myObject;
  ```

* ## default values and aliases
  You can provide default values for variables during destructuring, which will be used if the object property or array element doesn't exist:
  ```js
  const { name = 'Anonymous', age } = person;
  ```

* ## nested destructuring
  Destructuring can also be used with nested objects and arrays:
  ```js
  const user = {
    id: 1,
    info: {
      firstName: 'Alice',
      lastName: 'Johnson',
    },
  };

  const { id, info: { firstName, lastName } } = user;

  console.log(id);        // 1
  console.log(firstName); // Alice
  console.log(lastName);  // Johnson
  ```


<br>

# ES6 Modules 

## Essentials for making this work
  * ### 1. In the browser 
    __Serve your file via a local server__
    Instead of opening your HTML file directly from the file system (using file://), serve your files through a local development server. This way, your application will have an origin (e.g., http://localhost:port) instead of "null," and the CORS issue won't occur.

    You can use popular development servers like http-server, live-server, or webpack-dev-server to serve your files locally. First, install a server of your choice globally or as a development dependency 
    (tip: I can use wamp server just to test)

  * ### 2.  In node js 
    In package.json make sure to add:   
      ``` json
      "type": "module", // Set this to "module"
      ```

## Exporting from a module
We have `named exports` and `default exports`  
**Named exports** 
```js
// Exporting individual items
export const name = "John";
export function sayHello() {
    console.log(`Hello, ${name}!`);
}
```

**Default exports**
```js
// Exporting a default item
const greeting = "Hello, World!";
export default greeting;
```

## Importing into a module 
we can use alisases 
```js
import func as someName
```

**importing named exports**
```js
import { name, sayHello } from "./module.js";
console.log(name); // "John"
sayHello(); // "Hello, John!"
```
**importing default exports** We can name it as we wish, it is not a must to have the same name as the export name
```js
import greeting from "./module.js";
console.log(greeting); // "Hello, World!"
```

## CommonJS vs. ES6 Modules
ES6 modules are more modern and have some advantages over CommonJS modules (the previous standard in Node.js). They have a standard syntax, support for asynchronous loading, and better static analysis.




