const fs = require("fs");
const fetch = require("node-fetch");

const date = '1941-07-22'

let text_str = ''
let text_arr = []
let o = {}


//const header = "id","name","age","sex","link","text"

   const getData =  fetch(`https://prozhito.org/api/notes/search?search_type=diaries&date=${date}`)
    .then(res => res.json())
    .then(j=> j.data)
    .then( d=> o={
       id:notes[i]['text'],
    } ).then(o=>console.log(o))


console.log(o)
//        let DATA = []
//     for (i = 0; i < j.length; i++) {
//         DATA[i] = {
//             id: j.data.notes[i]['id'],
//             // name: json.data.notes[i]['person']['lastName'],
//             // age: json.data.notes[i]['age'],
//             // sex: json.data.notes[i]['person']['gender'],
//             // text: json.data.notes[i]['text']
//         }
//         // DATA.push(DATA[i])
//
//     }
//     return DATA
// }
//
// ).then(d=>console.log(d))
//
//

//console.log(DATA)

// function generateArray() {
//     names = ["Fariz", "Falisha", "Mami", "Defina", "Fiska", "Papi"];
//     newObj = [];
//
//     for (i = 0; i < n

console.log(' csv fetch request done')

//         newObj[i] = {
//             name: names[(Math.floor(Math.random() * (names.length)))],
//             age: Math.floor(Math.random() * 40),
//             communication: Math.floor(Math.random() * 20),
//             skill: Math.floor(Math.random() * 20),
//             experience: Math.floor(Math.random() * 20)
//         }
//     }
//
//     return newObj;
// }
//
// console.log(generateArray());

