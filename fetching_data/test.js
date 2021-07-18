function generateArray() {
    names = ["Fariz", "Falisha", "Mami", "Defina", "Fiska", "Papi"];
    newObj = [];

    for (i = 0; i < names.length; i++) {
        newObj[i] = {
            name: 1,

        }
    }

    return newObj;
}

console.log(generateArray())