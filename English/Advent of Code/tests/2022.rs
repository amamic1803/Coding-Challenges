use std::process::Command;


#[test]
fn day_01_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("1")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "69289");
}

#[test]
fn day_01_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("1")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "205615");
}

#[test]
fn day_02_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("2")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "11873");
}

#[test]
fn day_02_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("2")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "12014");
}

#[test]
fn day_03_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("3")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "7878");
}

#[test]
fn day_03_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("3")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "2760");
}

#[test]
fn day_04_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("4")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "540");
}

#[test]
fn day_04_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("4")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "872");
}

#[test]
fn day_05_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("5")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "NTWZZWHFV");
}

#[test]
fn day_05_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("5")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "BRZGFVBTJ");
}

#[test]
fn day_06_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("6")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1287");
}

#[test]
fn day_06_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("6")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "3716");
}

#[test]
fn day_07_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("7")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1432936");
}

#[test]
fn day_07_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("7")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "272298");
}

#[test]
fn day_08_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("8")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1829");
}

#[test]
fn day_08_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("8")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "291840");
}

#[test]
fn day_09_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("9")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "5858");
}

#[test]
fn day_09_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("9")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "2602");
}

#[test]
fn day_10_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("10")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "12880");
}

#[test]
fn day_10_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("10")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    let expected = "####..##....##..##..###....##.###..####.\n#....#..#....#.#..#.#..#....#.#..#.#....\n###..#.......#.#..#.#..#....#.#..#.###..\n#....#.......#.####.###.....#.###..#....\n#....#..#.#..#.#..#.#....#..#.#.#..#....\n#.....##...##..#..#.#.....##..#..#.####.";

    assert_eq!(stdout, expected);
}

#[test]
fn day_11_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("11")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "55944");
}

#[test]
fn day_11_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("11")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "15117269860");
}

#[test]
fn day_12_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("12")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "528");
}

#[test]
fn day_12_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2022")
        .arg("12")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "522");
}