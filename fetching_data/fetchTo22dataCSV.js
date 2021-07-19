const fs = require("fs");
const fetch = require("node-fetch");
const fastcsv = require('fast-csv');


const date = '1941-07-22'

let text_str = ''
let text_arr = []

fetch(`https://prozhito.org/api/notes/search?search_type=diaries&date=${date}`)
    .then(response => response.json())
    .then(json => json.data.notes)
    .then(function (notes) {
        o = []
        for (let i = 0; i < notes.length; i++) {
            o[i] = {

                "id":i+1,
                "name":`${notes[i]['person']['firstName']} ${notes[i]['person']['thirdName']} ${notes[i]['person']['lastName']}`,
                 "age":`${notes[i]['age']}`,
                 "sex":`${notes[i]['person']['gender']}`,
                "link":'undefined',
                "text":`${notes[i].text}`
            }

        }
        return o } )
.then(function (data){
    const ws = fs.createWriteStream("C:\\Users\\yayar\\OneDrive\\Рабочий стол\\b2\\sonicDataAnalizeYaro\\csv\\22Data.csv");
    fastcsv
        .write(data, { headers: true })
        .pipe(ws);
})


console.log('fetch to csv  done')
