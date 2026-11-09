pub fn a17(){
    // 3 ways to make string variable
    let s: &str = "Hello";
    let mut s1 = "Hello".to_string();
    let mut s2 = String::from("Hello");

    s2.push_str(" World"); // Push one string
    s1.push('!'); // Push one character

    println!("{}",s2);
    println!("{}",s1);
    println!("");

    let result = format!("{} {} {}",s,s1,s2); // Concat strings
    println!("{}",result);
    println!("");

    let result1 = s1 + " " + &s2; // Another way to concat strings
    println!("{}",result1);

    println!("{}",s.len()); //finding length of string
}