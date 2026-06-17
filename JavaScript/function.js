// function addNumbers(a,b){
//     const total= a+b;
//     return total;
// }

// const addition=addNumbers(10,24);

//---------------------> add multiple numbers:-

// function addNumbers(...numbers){
//     let total=0;
//     numbers.forEach(num=>{
//         total=total+num;
//     }
        
//     )
//     return total;
// }
// const addTotal=addNumbers(1,2,3,4,5,5);

//---------------------> add function in an object:-
// let falvor="butterScotch";
const fridge={
    "items": "mango",
    "water": "bottle",
    "icecream":function(flavor){
        console.log(`my fav falvor is ${flavor}`)
    },
    water(){
        console.log("chill");
    }
}

fridge.icecream("choco");
fridge.water();