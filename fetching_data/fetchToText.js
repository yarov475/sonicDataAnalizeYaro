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
                text_str += `#${notes[i].text}`            }
            return text_str
        }
    ).then(str => fs.writeFileSync("22_notes_fetched.txt", text_str))

console.log('fetch to text  done: 22_notes_fetched.txt')
