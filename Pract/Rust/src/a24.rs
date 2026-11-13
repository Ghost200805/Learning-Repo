pub fn a24(){ // A struct (short for "structure") is a custom data structure that lets you group related values together
    struct Person {
        name: String,
        age: u32,
    }

    let mut user = Person {
        name: String::from("John"),
        age: 35,
    };

    user.age = 36; // Change value of age
    println!("Name: {}", user.name);
    println!("Updated age: {}", user.age);
}