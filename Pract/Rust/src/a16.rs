pub fn a16(){
    // no need to define i before using it in for , unlike other languages
    for i in 1..6 { // Exlusive range (exlude 6)
        println!("i is: {}", i);
    }
    println!("");
    for i in 1..=6 { // Inclusive range (inclusive of 6)
        println!("i is: {}", i);
    }
}