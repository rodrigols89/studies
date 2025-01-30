function func() {
    var a = "Geeks";
    let b = "Geeks";

    if (true) {
        let a = "GeeksforGeeks"; // Legal Shadowing
        var b = "Geeks"; // Illegal Shadowing
        console.log(a); // It will print 'GeeksforGeeks'
        console.log(b); // It will print error
    }
}
func();
