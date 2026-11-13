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
use crate::a18::a18;
use crate::a19::a19;
use crate::a20::a20;
use crate::a21::a21;
use crate::a22::a22;
use crate::a23::a23;
use crate::a24::a24;
use crate::a25::a25;
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
mod a18;
mod a19;
mod a20;
mod a21;
mod a22;
mod a23;
mod a24;
mod a25;

fn main() { // u always need to start function in rust
    println!("Hello World!");
    println!("I am learning Rust.");
    println!("It is awesome!");

    println!("\na1 file content ----------------------\n");
    a1();
    println!("\na2 file content ----------------------\n");
    a2();
    println!("\na3 file content ----------------------\n");
    a3();
    println!("\na4 file content ----------------------\n");
    a4();
    println!("\na5 file content ----------------------\n");
    a5();
    println!("\na6 file content ----------------------\n");
    a6();
    println!("\na7 file content ----------------------\n");
    a7();
    println!("\na8 file content ----------------------\n");
    a8();
    println!("\na9 file content ----------------------\n");
    a9();
    println!("\na10 file content ---------------------\n");
    a10();
    println!("\na11 file content ---------------------\n");
    a11();
    println!("\na12 file content ---------------------\n");
    a12();
    println!("\na13 file content ---------------------\n");
    a13();
    println!("\na14 file content ---------------------\n");
    a14();
    println!("\na15 file content ---------------------\n");
    a15();
    println!("\na16 file content ---------------------\n");
    a16();
    println!("");
    
    // making functions and calling them
    fn add(a: i32, b: i32) -> i32 {
        a + b
    }

    let sum = add(3, 4);
    println!("Sum is: {}", sum);
    
    println!("\na17 file content ---------------------\n");
    a17();
    println!("\na18 file content ---------------------\n");
    a18();
    println!("\na19 file content ---------------------\n");
    a19();
    println!("\na20 file content (DSA) ---------------\n");
    a20();
    println!("\na21 file content ---------------------\n");
    a21();
    println!("\na22 file content ---------------------\n");
    a22();
    println!("\na23 file content ---------------------\n");
    a23();
    println!("\na24 file content ---------------------\n");
    a24();
    println!("\na25 file content ---------------------\n");
    a25();


}

/*
This is multiline comment.
It is similar to c/c++ language
 */