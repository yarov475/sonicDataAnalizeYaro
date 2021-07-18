const fs = require("fs");
const fetch = require("node-fetch");

const date = '1941-07-22'

let text_str = ''
let text_arr = []


//const header = "id","name","age","sex","link","text"

const promise = fetch(`https://prozhito.org/api/notes/search?search_type=diaries&date=${date}`)
    .then(response => response.json())
    .then(function(j) {
        let genObj= (j)=> {

            let DATA = []
            for (i = 0; i < j.length; i++) {
                DATA[i] = {
                    id: j.data.notes[i]['id'],
                    // name: json.data.notes[i]['person']['lastName'],
                    // age: json.data.notes[i]['age'],
                    // sex: json.data.notes[i]['person']['gender'],
                    // text: json.data.notes[i]['text']
                }
            }
            return DATA
        }



    });




console.log(' csv fetch request done')

// function generateArray() {
//     names = ["Fariz", "Falisha", "Mami", "Defina", "Fiska", "Papi"];
//     newObj = [];
//
//     for (i = 0; i < names.length; i++) {
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
/*
{
    id: 169785,
        diary: 622,
    text: 'Поговаривают о скором переводе детей в город. Некоторые матери профилактически снимают себе в городе комнату. С каждым дней количество приехавши матерей все увеличивается.',
    date: '1941-07-22',
    julian_date: null,
    dateTop: '0000-00-00',
    notDated: 0,
    julian_calendar: 0,
    user: 4,
    createdDate: 1476381597,
    pictures: 1,
    age: 42,
    comments: [],
    hidden_note: false,
    snippet: '',
    tags: [],
    mentioned_people: [],
    person: {
    id: 612,
        firstName: 'Анна',
        lastName: 'Рапопорт',
        thirdName: 'Менделеевна',
        birthDay: '1 мая 1899',
        deathDay: '5 декабря 1990',
        birthDay2: '0000-00-00',
        deathDay2: '0000-00-00',
        ageAround: 0,
        info: '',
        edition: '',
        additional_info: '',
        forVolunteers: '',
        diary: [],
        wikiLink: '',
        avatar: '/pictures/persons/612/preview_140x175.png?',
        diary_title: '',
        memories_title: '',
        memories_annotation: '',
        pictures: [],
        gender: 0,
        nickname: '',
        createdDate: 1626614951,
        updated: null
},
    diary_data: {
        id: 622,
            person: 612,
            statuses: [ '2' ],
            notes: 37,
            premier: 1,
            type: 1,
            types: [ [Object] ],
            disable_weight_sort: 0,
            tags: [],
            firstNote: '1941-07-01',
            lastNote: '1941-10-15',
            createdDate: 1626614951,
            title: '',
            description: ''
    }
}
*/
