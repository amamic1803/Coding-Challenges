use crate::shared::structures::Day;
use std::iter;

pub fn day_09() -> Day {
    Day::new(9, include_str!("text.txt"), include_str!("input.txt"), part1, part2)
}

fn part1(input: &str) -> String {
    compress1(input).enumerate().map(|(i, block)| i as u64 * block as u64).sum::<u64>().to_string()
}

fn part2(input: &str) -> String {
    compress2(input).enumerate().map(|(i, block)| i as u64 * block as u64).sum::<u64>().to_string()
}

fn compress1(disc: &str) -> impl Iterator<Item = u32> {
    let mut disc = disc.trim().chars().map(|c| c.to_digit(10).unwrap() as u8).collect::<Vec<_>>();
    if disc.len() % 2 == 0 {
        disc.pop();
    }
    let mut i = 0;
    iter::from_fn(move || loop {
        if i >= disc.len() {
            return None;
        }

        if disc[i] != 0 {
            disc[i] -= 1;
            return Some(i as u32 >> 1);
        }

        let last_ind = disc.len() - 1;
        if disc[last_ind] != 0 {
            if disc[i + 1] != 0 {
                disc[i + 1] -= 1;
                disc[last_ind] -= 1;
                return Some(last_ind as u32 >> 1);
            } else {
                i += 2;
            }
        } else {
            disc.pop();
            disc.pop();
        }
    })
}

fn compress2(disc: &str) -> impl Iterator<Item = u32> {
    let mut compacted_disc = Vec::with_capacity(20000 * 9);
    for (i, c) in disc.trim().chars().enumerate() {
        let amount = c.to_digit(10).unwrap() as u8;
        let data = if i % 2 == 0 { Some(i) } else { None };
        compacted_disc.extend(iter::repeat(data).take(amount as usize));
    }

    compacted_disc.into_iter().map(|data| data.unwrap_or(0) as u32)
}
