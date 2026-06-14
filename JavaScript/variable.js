var name="sagar kumar";
console.log(name);

// let and const 
// let banana=12;
// const height="5'10"; ---> //immutable 

if(name=="sagar kumar"){
    let banana=12;  // if we change this to 'var' than this will work
    const height="5'10"; 
}
// console.log(banana); ---> gives an error as it's a "let" variable and outside the curly bracket.
// console.log(height);  --->gives an error as it's a "const" variable and outside the curly bracket.