const fs = require("fs");
const fetch = require("node-fetch");

const date = '1941-07-22'

let text_str = ''
let text_arr = []

fetch(`https://prozhito.org/api/notes/search?search_type=diaries&date=${date}`)
    .then(response => response.json())
    .then(json => json.data.notes)
    .then(function (notes) {
        ar = []
        O={};
            for (let i = 0; i < notes.length; i++) {
                O[i] = {
                    "id":i,
                    "name"
                }

                 \n ФИО: ${notes[i]['person']['firstName']} ${notes[i]['person']['thirdName']} ${notes[i]['person']['lastName']}
                    \nвозраст ${notes[i]['age']}
            \n пол ${notes[i]['person']['gender']};
            \n запись \n
                ${notes[i].text}
            \n .


            }
             ar.push(O)
        }
    ).then(str => console.log(str))


console.log('fetch to text  done: 22_notes_fetched.txt')
