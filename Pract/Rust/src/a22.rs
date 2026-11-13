pub fn a22(){
    let a = ("Ram",5,true);
    println!("First element in tuple: {}",a.0); // This is how first element is retireved in a tuple

    let (name,age,bool) = a; // This is called unpacking using tuple, storing values in these variables
    println!("name = {} age = {} bool = {}",name,age,bool);

    fn get_user() -> (String, i32) {
        (String::from("Liam"), 25)
    }

    let user = get_user();
    println!("User: {} ({} years old)", user.0, user.1);
}