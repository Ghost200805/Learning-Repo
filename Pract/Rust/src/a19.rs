// Borrowing value from another variable

pub fn a19(){
    let a = String::from("Hello");
    let b = &a;

    println!("a = {}", a);
    println!("b = {}", b);
}