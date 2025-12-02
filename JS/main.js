import U, { printAge as PA, printName } from './user.js'

const user  = new U('Hamza', 23)

let myFunction = {
    hidden1:PA,
    hidden2:printName
}

myFunction.hidden1(user)
printName(user)





