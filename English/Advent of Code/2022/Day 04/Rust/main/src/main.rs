fn main() {
    let input = include_str!("../../../input.txt");
    let mut contain: u64 = 0;
    let mut overlap: u64 = 0;
    let mut elves: Vec<u64>;
    for line in input.trim().split("\n") {
        elves = vec![];
        for elf in line.split(",") {
            for sectors in elf.split("-") {
                elves.push(sectors.parse::<u64>().unwrap())
            }
        }
        if ((elves[0] <= elves[2]) && (elves[1] >= elves[3])) ||
            ((elves[2] <= elves[0]) && (elves[3] >= elves[1])) {
            contain += 1;
            overlap += 1;
        } else if ((elves[0] >= elves[2]) && (elves[0] <= elves[3])) ||
            ((elves[1] >= elves[2]) && (elves[1] <= elves[3])) {
            overlap += 1;
        }
    }
    println!("{}\n{}", contain, overlap);
}
