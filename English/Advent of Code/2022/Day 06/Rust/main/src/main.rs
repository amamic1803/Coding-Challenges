fn main() {
    let input = include_str!("../../../input.txt");
    let mut characters = 4;
    while !start_of_packet(&input[(characters - 4)..characters]) {
        characters += 1;
    }
    println!("{}", characters);
    let mut characters = 14;
    while !start_of_packet(&input[(characters - 14)..characters]) {
        characters += 1;
    }
    println!("{}", characters);
}

fn start_of_packet(inp: &str) -> bool {
    for x in inp.chars() {
        let mut counted = 0;
        for y in inp.chars() {
            if x == y {counted += 1;}
        }
        if counted > 1 {return false}
    }
    return true
}
