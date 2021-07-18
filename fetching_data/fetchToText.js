const fs = require("fs");
const fetch = require("node-fetch");

const date = '1941-07-22'

let text_str = ''
let text_arr = []

fetch(`https://prozhito.org/api/notes/search?search_type=diaries&date=${date}`)
    .then(response => response.json())
    .then(json => json.data.notes)
    .then(function (notes) {
            for (let i = 0; i < notes.length; i++) {
                text_str += ` \n Запись N ${i + 1}
            \n ФИО: ${notes[i]['person']['firstName']} ${notes[i]['person']['thirdName']} ${notes[i]['person']['lastName']}
               \nвозраст ${notes[i]['age']} 
             \n пол ${notes[i]['person']['gender']};
            \n запись \n 
            ${notes[i].text}
            \n ..........................................................................................................`
            }
            return text_str //text_arr
        }
    ).then(str => fs.writeFileSync("22_notes_fetched.txt", text_str))


console.log('fetch to text  done: 22_notes_fetched.txt')
