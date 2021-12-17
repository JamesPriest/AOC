use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];


    println!("In file {}", filename);
    let soln1 = part_one(filename);
    println!("Number of increases --> {:?}", soln1);

    let soln2 = part_two(filename);
    println!("Number of increases --> {:?}", soln2);


}

fn part_one(filename: &str) -> i32 {
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut split = contents.split("\n");

    let mut increase_counter = 0;
    let mut curr_measurement;
    // Read off the first value 
    let mut prev_measurement = split.next().expect("Failure").parse::<i32>().unwrap();
    for s in split {
        curr_measurement = match s.parse::<i32>() {
            Ok(n) => n,
            Err(_e) => -1,
        };
        // println!("curr_measurement is {:?}", curr_measurement);
        if curr_measurement > prev_measurement {
            increase_counter += 1;
        }
        else if curr_measurement == -1 {
            continue;
        }
        prev_measurement = curr_measurement

    }
    increase_counter
}

fn part_two(filename: &str) -> i32 {
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut split = contents.split("\n");
    let mut increase_counter = 0;

    let mut past_3 = split.next().expect("Failure").parse::<i32>().unwrap();
    let mut past_2 = split.next().expect("Failure").parse::<i32>().unwrap();
    let mut past_1 = split.next().expect("Failure").parse::<i32>().unwrap();
    
    let mut curr_measurement;

    for s in split {
        curr_measurement = match s.parse::<i32>() {
            Ok(n) => n,
            Err(_e) => -1,
        };
        // println!("curr_measurement is {:?}", curr_measurement);
        if curr_measurement > past_3 {
            increase_counter += 1;
        }
        else if curr_measurement == -1 {
            continue;
        }
        past_3 = past_2;
        past_2 = past_1;
        past_1 = curr_measurement;

    }
    increase_counter
}