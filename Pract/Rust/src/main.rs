use crate::a1::a1;
use crate::a2::a2;
use crate::a3::a3;
use crate::a4::a4;
use crate::a5::a5;
use crate::a6::a6;
mod a2;
mod a1;
mod a3;
mod a4;
mod a5;
mod a6;

fn main() { // u always need to start function in rust
    println!("Hello World!");
    println!("I am learning Rust.");
    println!("It is awesome!");
    println!("");
    println!("a1 file content ----------------------");
    a1();
    println!("");
    println!("a2 file content ----------------------");
    a2();
    println!("");
    println!("a3 file content ----------------------");
    a3();
    println!("");
    println!("a4 file content ----------------------");
    a4();
    println!("");
    println!("a5 file content ----------------------");
    a5();
    println!("");
    println!("a6 file content ----------------------");
    a6();

}

/*
This is multiline comment.
It is similar to c/c++ language
 */