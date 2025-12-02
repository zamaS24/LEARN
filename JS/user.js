export default class User {
    constructor(name, age) {
        this.age =  age; 
        this.name = name; 
    } 
}

export function printName(user) {
    console.log(`Name is : ${user.name}`)
}

export function printAge(user) {
    console.log(`Age is : ${user.age}`)
}


