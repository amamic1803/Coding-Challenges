fn main() {
    let input = include_str!("input.txt");
    let mut num_of_piles: u64 = 0;
    for line in input.split("\n") {
        if !line.contains("[") {
            num_of_piles = line.trim().rsplit_once(" ").unwrap().1.parse::<u64>().unwrap();
            break;
        }
    }
    let mut piles: Vec<Vec<char>> = vec![];
    for _ in 0..num_of_piles {
        piles.push(vec![]);
    }
    let mut move_vec: Vec<&str>;
    for line in input.split("\n") {
        if line.contains("[") {
            let mut ind = 0;
            let mut found_items: u64 = 1;
            for character in line.chars() {
                if ind == (1 + (found_items - 1) * 4) {
                    if character != " ".chars().next().unwrap() {
                        piles[(found_items as usize) - 1].insert(0, character);
                    }
                    found_items += 1;
                }
                if found_items == num_of_piles + 1 {break;}
                ind += 1;
            }
        } else if line.contains("move") {
            move_vec = line.trim().split(" ").collect();
            for _ in 0..move_vec[1].parse::<usize>().unwrap() {
                let character: char = piles[move_vec[3].parse::<usize>().unwrap() - 1][piles[move_vec[3].parse::<usize>().unwrap() - 1].len() - 1];
                piles[move_vec[5].parse::<usize>().unwrap() - 1].push(character);
                piles[move_vec[3].parse::<usize>().unwrap() - 1].pop();
            }
        }
    }
    let mut output: String = String::new();
    for indeks in 0..(num_of_piles as usize) {
        output.push(piles[indeks][piles[indeks].len() - 1]);
    }
    println!("{}", output);

    let mut piles: Vec<Vec<char>> = vec![];
    for _ in 0..num_of_piles {
        piles.push(vec![]);
    }
    let mut move_vec: Vec<&str>;
    for line in input.split("\n") {
        if line.contains("[") {
            let mut ind = 0;
            let mut found_items: u64 = 1;
            for character in line.chars() {
                if ind == (1 + (found_items - 1) * 4) {
                    if character != " ".chars().next().unwrap() {
                        piles[(found_items as usize) - 1].insert(0, character);
                    }
                    found_items += 1;
                }
                if found_items == num_of_piles + 1 {break;}
                ind += 1;
            }
        } else if line.contains("move") {
            move_vec = line.trim().split(" ").collect();
            let insert_ind = piles[move_vec[5].parse::<usize>().unwrap() - 1].len();
            for _ in 0..move_vec[1].parse::<usize>().unwrap() {
                let character: char = piles[move_vec[3].parse::<usize>().unwrap() - 1][piles[move_vec[3].parse::<usize>().unwrap() - 1].len() - 1];
                piles[move_vec[5].parse::<usize>().unwrap() - 1].insert(insert_ind, character);
                piles[move_vec[3].parse::<usize>().unwrap() - 1].pop();
            }
        }
    }
    let mut output: String = String::new();
    for indeks in 0..(num_of_piles as usize) {
        output.push(piles[indeks][piles[indeks].len() - 1]);
    }
    println!("{}", output);
}
