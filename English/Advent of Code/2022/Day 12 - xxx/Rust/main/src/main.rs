use std::collections::HashMap;
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

fn main() {
    let input = include_str!("../../../input.txt");

    let mut height_map: Vec<Vec<i64>> = vec![];
    let mut location_init: [i64; 2] = [0; 2];
    let mut location_dest: [i64; 2] = [0; 2];
    for (curr_row, line) in input.trim().split('\n').enumerate() {
        let mut current_row: Vec<i64> = vec![];
        for (curr_col, x) in line.chars().enumerate() {
            if x == 'S' {
                location_init = [curr_col as i64, curr_row as i64];
            } else if x == 'E' {
                location_dest = [curr_col as i64, curr_row as i64];
            }
            current_row.push(char_value(x));
        }
        height_map.push(current_row);
    }

    let mut recursion_results: HashMap<u64, Option<i64>> = HashMap::new();

    println!("{}", find_path(&mut height_map, location_init, location_dest, &mut recursion_results).unwrap() - 1);
}

fn find_path(height_map: &mut Vec<Vec<i64>>, location_curr: [i64; 2], location_dest: [i64; 2], recursion_results: &mut HashMap<u64, Option<i64>> ) -> Option<i64> {
    let original_value = height_map[location_curr[1] as usize][location_curr[0] as usize];
    height_map[location_curr[1] as usize][location_curr[0] as usize] = - 1;
    let mut result: Option<i64> = None;

    let mut current_hash = DefaultHasher::new();
    let _ = &height_map.hash(&mut current_hash);
    let current_hash = current_hash.finish();

    match recursion_results.get(&current_hash) {
        Some(t) => result = *t,
        None => {
            if location_curr == location_dest {
                result = Some(0);
            } else {
                if (location_curr[0] >= 1) && (height_map[location_curr[1] as usize][(location_curr[0] - 1) as usize] - original_value <= 1) && (height_map[location_curr[1] as usize][location_curr[0] as usize - 1] != -1) {
                    if let Some(t) = find_path(height_map, [location_curr[0] - 1, location_curr[1]], location_dest, recursion_results) {
                        if let Some(res) = result {
                            if t < res { result = Some(t); }
                        } else { result = Some(t); }
                    }
                }
                if (location_curr[0] < (height_map[0].len() as i64 - 1)) && (height_map[location_curr[1] as usize][(location_curr[0] + 1) as usize] - original_value <= 1) && (height_map[location_curr[1] as usize][location_curr[0] as usize + 1] != -1) {
                    if let Some(t) = find_path(height_map, [location_curr[0] + 1, location_curr[1]], location_dest, recursion_results) {
                        if let Some(res) = result {
                            if t < res { result = Some(t); }
                        } else { result = Some(t); }
                    }
                }
                if (location_curr[1] >= 1) && (height_map[(location_curr[1] - 1) as usize][location_curr[0] as usize] - original_value <= 1) && (height_map[location_curr[1] as usize - 1][location_curr[0] as usize] != -1) {
                    if let Some(t) = find_path(height_map, [location_curr[0], location_curr[1] - 1], location_dest, recursion_results) {
                        if let Some(res) = result {
                            if t < res { result = Some(t); }
                        } else { result = Some(t); }
                    }
                }
                if (location_curr[1] < (height_map.len() as i64 - 1)) && (height_map[(location_curr[1] + 1) as usize][location_curr[0] as usize] - original_value <= 1) && (height_map[location_curr[1] as usize + 1][location_curr[0] as usize] != -1) {
                    if let Some(t) = find_path(height_map, [location_curr[0], location_curr[1] + 1], location_dest, recursion_results) {
                        if let Some(res) = result {
                            if t < res {result = Some(t);}
                        } else {result = Some(t);}
                    }
                }
            }

            if let Some(t) = result {
                result = Some(t + 1);
            }

            recursion_results.insert(current_hash, result);
        }
    }

    height_map[location_curr[1] as usize][location_curr[0] as usize] = original_value;
    result
}

fn char_value(character: char) -> i64 {

    match character {
        'S' => 0_i64,
        'E' => 25_i64,
        _ => {
            let mut curr_val: i64 = 0;
            for x in ALPHABET.chars() {
                if x == character {
                    break;
                }
                curr_val += 1;
            }
            curr_val
        }
    }

}

static ALPHABET: &str = "abcdefghijklmnopqrstuvwxyz";

