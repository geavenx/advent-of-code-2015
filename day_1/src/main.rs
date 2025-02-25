use std::fs;

fn main() {
    // part_one();
    part_two();
}

fn part_one() {
    let file_path = "input.txt";
    let input = fs::read_to_string(file_path).expect("Shuold have been able to read the file.");

    let mut list: Vec<char> = input.chars().collect();
    list.sort();

    let mut floor: i32 = 0;

    for ch in list.iter() {
        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => (),
        }
    }

    println!("{}", floor);
}

fn part_two() {
    let file_path = "input.txt";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file.");

    let mut list: Vec<char> = input.chars().collect();

    let mut floor: i32 = 0;

    for (idx, ch) in list.into_iter().enumerate() {
        println!("{}", floor);
        if floor == -1 {
            println!("PART TWO: {}", idx);
            return;
        }

        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => (),
        }
    }
}
