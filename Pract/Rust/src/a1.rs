pub fn a1(){
    let n = "Robin";
    let mut a = 5; // use mut to specify its mutable (can be changed), if u want to change in future..
    println!("My name is {}",n);

    println!("Before number : {}",a);
    a = 10;
    println!("After Number : {}",a);
}