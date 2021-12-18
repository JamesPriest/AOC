use std::env;
use std::fs;

#[derive(Debug)]
struct SubPosition {
    depth: i32,
    horizontal: i32,
}

impl SubPosition {
    pub fn increase_depth(&mut self, value: i32) {
        self.depth += value;
    }

    pub fn decrease_depth(&mut self, value: i32) {
        self.depth -= value;
    } 
    
    pub fn move_forward(&mut self, value: i32) {
        self.horizontal += value;
    }    
}

#[derive(Debug)]
struct SubPositionPt2 {
    depth: i32,
    horizontal: i32,
    aim: i32,
}

impl SubPositionPt2 {
    pub fn down(&mut self, value: i32) {
        self.aim += value;
    }

    pub fn up(&mut self, value: i32) {
        self.aim -= value;
    } 
    
    pub fn move_forward(&mut self, value: i32) {
        self.horizontal += value;
        self.depth += value * self.aim;
    }    
}


fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];


    println!("In file {}", filename);
    


    // println!("Sub final values: {:?}", sub)
    
    let soln1 = part_one(filename);
    println!("Sub combination: {}", soln1);

    let soln2 = part_two(filename);
    println!("Sub combination: {}", soln2);    
}

fn part_one(filename: &str) -> i32 {
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut split = contents.split("\n");
    let mut _vals: Vec<String>;
    let mut direction: String;
    let mut magnitude: i32;

    let mut sub = SubPosition {depth: 0, horizontal: 0};

    for s in split {
        // println!("s is: {:?}", s);
        _vals = s.split(" ").map(
            |val| val.parse().unwrap()
        ).collect();

        if _vals.len() == 2 {
            // println!("_vals is: {:?}", _vals);
            magnitude = _vals.pop().expect("Failed to get Mag").parse::<i32>().unwrap();
            // println!("direction is: {:?}", magnitude);
            direction = _vals.pop().expect("Failed to get Direction");

            match direction.as_ref() {
                "forward" => sub.move_forward(magnitude),
                "down" => sub.increase_depth(magnitude),
                "up" => sub.decrease_depth(magnitude),
                _ => println!("Something else?: {}", direction),
            }
        }
        else {
            continue;
        }

        // println!("a is: {} and b is: {}", magnitude, direction);

    }
    sub.depth * sub.horizontal
}

fn part_two(filename: &str) -> i32 {
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut split = contents.split("\n");
    let mut _vals: Vec<String>;
    let mut direction: String;
    let mut magnitude: i32;

    let mut sub = SubPositionPt2 {depth: 0, horizontal: 0, aim: 0};

    for s in split {
        // println!("s is: {:?}", s);
        _vals = s.split(" ").map(
            |val| val.parse().unwrap()
        ).collect();

        if _vals.len() == 2 {
            // println!("_vals is: {:?}", _vals);
            magnitude = _vals.pop().expect("Failed to get Mag").parse::<i32>().unwrap();
            // println!("direction is: {:?}", magnitude);
            direction = _vals.pop().expect("Failed to get Direction");

            match direction.as_ref() {
                "forward" => sub.move_forward(magnitude),
                "down" => sub.down(magnitude),
                "up" => sub.up(magnitude),
                _ => println!("Something else?: {}", direction),
            }
        }
        else {
            continue;
        }

        // println!("a is: {} and b is: {}", magnitude, direction);

    }
    sub.depth * sub.horizontal
}