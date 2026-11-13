pub fn a21(){
    let n = [1,2,3,4,5]; // to change values in array use mut before variable name (mutable)
    println!("{:?}",n); // To print whole array
    for i in n{
        println!("Number = {}",i);
    }

    let fruits = vec!["apple", "banana", "orange"];
    for fruit in &fruits { // in vectors we use & , whereas in array we directly write variable name
        println!("I like {}.", fruit);
    }
}