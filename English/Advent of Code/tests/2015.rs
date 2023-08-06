use std::process::Command;


#[test]
fn year_2015_day_01_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("1")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "232");
}

#[test]
fn year_2015_day_01_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("1")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1783");
}

#[test]
fn year_2015_day_02_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("2")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1588178");
}

#[test]
fn year_2015_day_02_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("2")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "3783758");
}

#[test]
fn year_2015_day_03_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("3")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "2081");
}

#[test]
fn year_2015_day_03_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("3")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "2341");
}

#[test]
fn year_2015_day_04_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("4")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "254575");
}

#[test]
fn year_2015_day_04_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("4")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1038736");
}

#[test]
fn year_2015_day_05_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("5")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "255");
}

#[test]
fn year_2015_day_05_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("5")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "55");
}

#[test]
fn year_2015_day_06_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("6")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "377891");
}

#[test]
fn year_2015_day_06_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2015")
        .arg("6")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "14110788");
}
