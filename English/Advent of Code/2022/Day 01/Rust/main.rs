fn main() {
    let input = include_str!("../input.txt");
    let mut elf_calories: Vec<u64> = vec![];
    let mut curr_calorie: u64 = 0;
    for line in input.split("\n") {
        if line != "" {
            curr_calorie += line.parse::<u64>().unwrap();
        } else {
            elf_calories.push(curr_calorie);
            curr_calorie = 0;
        }
    }
    elf_calories.sort();
    println!("{}\n{}", elf_calories[elf_calories.len() - 1], elf_calories[(elf_calories.len() - 3)..].iter().sum::<u64>());
}
