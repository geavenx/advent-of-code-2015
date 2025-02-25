use std::fs;

fn main() {
    let file_path = "input.txt";
    let input = fs::read_to_string(file_path).expect("Shuold have been able to read the file.");
}
