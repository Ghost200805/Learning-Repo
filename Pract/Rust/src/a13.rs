pub fn a13(){
    let mut count = 1;

    loop { // it runs forever if we dont use break ...
        println!("Hello World!");

        if count == 3 {
            break;
        }

        count += 1;
    }
}