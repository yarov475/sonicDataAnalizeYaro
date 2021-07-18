const fetch = require("node-fetch");
fetch('https://prozhito.org/api/notes/search?search_type=diaries&date=1941-07-22')
    .then(response => response.json())
    .then(json =>
        console.log( json.data.notes[1].text))
