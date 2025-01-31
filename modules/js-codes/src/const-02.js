function sayPerson(person) {
    console.log(person);
}

const person = {
    name: "Rodrigo",
    age: 28,
};
sayPerson(person);

person.name = "drigols - Software Engineer";
person.age = 15;
sayPerson(person);

// Freeze the object "person".
Object.freeze(person);

person.name = "Rodirgo Santoro";
person.age = 50;
sayPerson(person);
