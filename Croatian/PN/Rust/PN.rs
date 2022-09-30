use std::io::stdin;

fn main() {
    let mut upis1 = String::new();
    stdin().read_line(&mut upis1).expect("Failed to receive input!");
    let split1: Vec<&str> = upis1.split(' ').collect();
    let r1: i128 = split1[0].trim().parse().expect("Please type a number!");
    let s1: i128 = split1[1].trim().parse().expect("Please type a number!");

    let mut upis2 = String::new();
    stdin().read_line(&mut upis2).expect("Failed to receive input!");
    let split2: Vec<&str> = upis2.split(' ').collect();
    let r2: i128 = split2[0].trim().parse().expect("Please type a number!");
    let s2: i128 = split2[1].trim().parse().expect("Please type a number!");

    let jedinice_u_polju: i128 = (r2 - r1 + 1) * (s2 - s1 + 1);
    let vodoravno_zbrojeno: i128 = (r2 - r1 + 1) * (s2 * (s2 - 1) - (s1 - 1) * (s1 - 2));
    let mut vertikalno_zbrojeno: i128 = 0;

    let mut trenutni_broj: i128 = (r1 * r1 - (r1 % 2)) / 2 - r1 + 1;
    vertikalno_zbrojeno += trenutni_broj;
    let mut pomak_0: i128 = {
        if r1 % 2 == 1 {
            r1
        } else {
            r1 - 1
        }
    };
    let mut pomak_1: bool = {
        if r1 % 2 == 0 {
            false
        } else {
            true
        }
    };

    for _i in (r1 + 1)..(r2 + 1) {
        if pomak_1 == true {
            pomak_0 += 2;
            vertikalno_zbrojeno += trenutni_broj + pomak_0;
            pomak_1 = false;
        } else {
            vertikalno_zbrojeno += trenutni_broj + pomak_0;
            pomak_1 = true;
        }
        trenutni_broj += pomak_0
    }
    vertikalno_zbrojeno *= s2 - s1 + 1;

    println!("{}", jedinice_u_polju + vodoravno_zbrojeno + vertikalno_zbrojeno)
}
