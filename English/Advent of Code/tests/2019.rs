use std::process::Command;


#[test]
fn day_01_part1() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2019")
        .arg("1")
        .arg("1")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "3328306");
}

#[test]
fn day_01_part2() {
    let output = Command::new("cargo")
        .arg("run")
        .arg("--")
        .arg("2019")
        .arg("1")
        .arg("2")
        .output()
        .unwrap();
    let stdout = String::from(String::from_utf8(output.stdout).unwrap().trim());

    assert_eq!(stdout, "4989588");
}