function generateArray() {
    names = ["Fariz", "Falisha", "Mami", "Defina", "Fiska", "Papi"];
    newObj = [];

    for (i = 0; i < names.length; i++) {
        newObj[i] = {
            name: names[(Math.floor(Math.random() * (names.length)))],
            age: Math.floor(Math.random() * 40),
            communication: Math.floor(Math.random() * 20),
            skill: Math.floor(Math.random() * 20),
            experience: Math.floor(Math.random() * 20)
        }
    }

    return newObj;
}

console.log(generateArray())