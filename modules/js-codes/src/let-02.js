function sayAnima(animal) {
    console.log(animal);
}

// Global SCOPE.
let animal = "Elephant";

/* SECOND SCOPE. */
{
    // Animal variable declared with "let" in the SECOND SCOPE.
    let animal = "cat";
    sayAnima(animal);

    animal = "catTwo";
    sayAnima(animal);
}

/* THIRD SCOPE. */
{
    // Animal variable declared  with "let" in THIRD SCOPE.
    let animal = "dog";
    sayAnima(animal);

    animal = "dogTwo";
    sayAnima(animal);
}
