use crate::a1::a1;
use crate::a2::a2;
use crate::a3::a3;
use crate::a4::a4;
use crate::a5::a5;
use crate::a6::a6;
use crate::a7::a7;
use crate::a8::a8;
use crate::a9::a9;
use crate::a10::a10;
use crate::a11::a11;
use crate::a12::a12;
use crate::a13::a13;
use crate::a14::a14;
use crate::a15::a15;
use crate::a16::a16;
use crate::a17::a17;
mod a2;
mod a1;
mod a3;
mod a4;
mod a5;
mod a6;
mod a7;
mod a8;
mod a9;
mod a10;
mod a11;
mod a12;
mod a13;
mod a14;
mod a15;
mod a16;
mod a17;

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
    println!("");
    println!("a7 file content ----------------------");
    a7();
    println!("");
    println!("a8 file content ----------------------");
    a8();
    println!("");
    println!("a9 file content ----------------------");
    a9();
    println!("");
    println!("a10 file content ---------------------");
    a10();
    println!("");
    println!("a11 file content ---------------------");
    a11();
    println!("");
    println!("a12 file content ---------------------");
    a12();
    println!("");
    println!("a13 file content ---------------------");
    a13();
    println!("");
    println!("a14 file content ---------------------");
    a14();
    println!("");
    println!("a15 file content ---------------------");
    a15();
    println!("");
    println!("a16 file content ---------------------");
    a16();
    println!("");
    
    // making functions and calling them
    fn add(a: i32, b: i32) -> i32 {
        a + b
    }

    let sum = add(3, 4);
    println!("Sum is: {}", sum);

    println!("a17 file content ---------------------");

    a17();
    println!("");
}

/*
This is multiline comment.
It is similar to c/c++ language
 */