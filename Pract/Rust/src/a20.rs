use std::collections::HashMap;

pub fn a20(){
    println!("\nArrays\n");

    let fruits = ["apple", "banana", "orange"];
    println!("Last fruit: {}", fruits[2]);

    println!("\nVectors\n");

    let mut fruits1 = vec!["apple", "banana"];
    fruits1.push("cherry");
    println!("Last fruit: {}", fruits1[2]);

    println!("\nTuples\n");

    let person = ("John", 30, true);
    println!("Name: {}", person.0);
    println!("Age: {}", person.1);
    println!("Is active: {}", person.2);

    println!("\nHash Maps\n");

    let mut capital_cities = HashMap::new();
    capital_cities.insert("France", "Paris");
    capital_cities.insert("Japan", "Tokyo");

    println!("Capital of Japan is {}", capital_cities["Japan"]);
}