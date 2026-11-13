pub fn a25(){ // An enum (short for "enumeration") is a way to define a type that can be one of a few different values.
    enum Direction {Up,Down,Left,Right}
    let my_direction = Direction::Left;

    match my_direction {
        Direction::Up => println!("Going up"),
        Direction::Down => println!("Going down"),
        Direction::Left => println!("Going left"),
        Direction::Right => println!("Going right"),
    }

    enum LoginStatus {Success(String), Error(String)}
    let result1 = LoginStatus::Success(String::from("Welcome, John!"));
    let result2 = LoginStatus::Error(String::from("Incorrect password"));

    match result1 {
        LoginStatus::Success(message) => println!("Success: {}", message),
        LoginStatus::Error(message) => println!("Error: {}", message),
    }
    match result2 {
        LoginStatus::Success(message) => println!("Success: {}", message),
        LoginStatus::Error(message) => println!("Error: {}", message),
    }
}