use std::collections::HashMap;

pub fn a23(){
    let mut c = HashMap::new();
    c.insert("Ram", 5);
    c.insert("Kanak", 6);
    c.insert("Sam", 7);
    println!("Printing whole HashMap : {:?}",c);

    if let Some(age) = c.get("Ram") { // Assigning value of hashmap to a variable
        println!("The age of Ram is {}.", age);
    } else {
        println!("Ram is not in the map.");
    }

    c.remove("Kanak");
    println!("{:?}",c);

    for (name,age) in &c{
        println!("Name = {} , Age = {}",name,age);
    }
}