use std::process::Command;


#[test]
fn day_01_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2021")
        .arg("1")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1791");
}

#[test]
fn day_01_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2021")
        .arg("1")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "1822");
}