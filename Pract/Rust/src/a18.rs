pub fn a18(){
    println!("");
    println!("scenario 1");
    let a = String::from("Hello");
    let b = a;
    // println!("{}", a); Error: a no longer owns the value
    println!("{}", b); // Ok: b now owns the value

    println!("");
    println!("scenario 2");
    let c = 5;
    let d = c;
    println!("c = {}", c);  // Works
    println!("d = {}", d);  // Works

    println!("");
    println!("scenario 3");
    let e = String::from("Hello");
    let f = e.clone(); // Now both have the same value
    println!("e = {}", e);  // Works
    println!("f = {}", f);  // Works
}