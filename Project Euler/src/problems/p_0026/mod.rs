//! **Problem 26** - *Reciprocal Cycles*
use crate::shared::structures::Problem;

/// Get `Problem` struct.
pub fn get_problem() -> Problem {
    Problem::new(26, "Reciprocal Cycles", solve)
}

use crate::shared::math::{gcd, ord};

const MAX_D: u64 = 1000;

fn solve() -> String {
    // the number of repeating digits in the decimal representation of 1/n
    // is equal to the multiplicative order of 10 modulo n
    // that is the smallest integer k such that 10^k = 1 (mod n)
    // for multiplicative order to exist, n must be coprime to 10
    // that is n must not have 2 or 5 as a factor

    let mut longest_d = 0;
    let mut longest_cycle = 0;

    for d in 2..MAX_D {
        if gcd(10, d) == 1 {
            let cycle_len = ord(10, d);
            if cycle_len > longest_cycle {
                longest_cycle = cycle_len;
                longest_d = d;
            }
        }
    }

    longest_d.to_string()
}

// old solution, uses long division
// fn solve() -> String {
//     let mut max_recurring_digits: u64 = 0;
//     let mut max_number: u64 = 0;
//
//     for d in 1..1000 {
//         let mut working_num: u64 = 1;
//         let mut result: Vec<u64> = vec![];
//
//         let mut recurring: bool = false;
//
//         while working_num != 0 {
//             working_num %= d;
//
//             if result.contains(&working_num) {
//                 recurring = true;
//                 result.push(working_num);
//                 break;
//             }
//             result.push(working_num);
//             working_num *= 10;
//
//         }
//
//         if recurring {
//             let mut length_recurring: u64 = 0;
//             for i in 0..(result.len()) {
//                 if (i != (result.len() - 1)) & (result[i] == result[result.len() - 1]) {
//                     length_recurring = ((result.len() - 1) - i) as u64;
//                 }
//             }
//
//             if length_recurring > max_recurring_digits {
//                 max_recurring_digits = length_recurring;
//                 max_number = d;
//             }
//
//         }
//
//     }
//
//     max_number.to_string()
// }
