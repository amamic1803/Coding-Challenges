use std::process::Command;


#[test]
fn day_01_part1() {
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
fn day_01_part2() {
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
fn day_02_part1() {
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
fn day_02_part2() {
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
fn day_03_part1() {
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
fn day_03_part2() {
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