// Add to Cargo.toml
// (under [dependencies])
// clearscreen = "1.0.10"

use std::io;
use std::io::Write;
use std::time::Duration;
use std::thread::sleep;
use std::f64::consts::PI;
use clearscreen;


fn main() {
    let radius: f64;
    let area: f64;

    loop {
        let mut radius_input = String::new();
        clearscreen::clear().unwrap();
        print!("\nRadius: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut radius_input).unwrap();
        radius_input = radius_input.replace(",", ".");

        match radius_input.trim().parse::<f64>() {
            Ok(r) => {
                radius = r;
                break;
            }
            Err(_) => {
                println!("\nInvalid input!");
                sleep(Duration::from_millis(1500));
                continue;
            }
        }
    }

    loop {
        let mut area_input = String::new();
        clearscreen::clear().unwrap();
        print!("\nRadius: {}\n\nSegment area: ", radius);
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut area_input).unwrap();
        area_input = area_input.replace(",", ".");

        match area_input.trim().parse::<f64>() {
            Ok(r) => {
                area = r;
                break;
            }
            Err(_) => {
                println!("\nInvalid input!");
                sleep(Duration::from_millis(1500));
                continue;
            }
        }
    }

    clearscreen::clear().unwrap();
    println!("\nRadius: {}\n\nSegment area: {}\n", radius, area);

    if radius.powi(2) * PI > area {
        println!("\nSegment height: {}", calc_segment_height(radius, area));
    } else {
        println!("\nSegment area bigger than possible!");
    }

    io::stdin().read_line(&mut String::new()).unwrap();
}

fn calc_segment_height(radius: f64, area: f64) -> f64 {
    let mut x0: f64 = radius;
    let mut x1: f64;
    let max_difference: f64 = 10.0_f64.powi((-(16 - len_of_number((radius as i128) * 2))) as i32);

    // Newton's method -> x1 = x0 - (f(x0))/(f'(x0))
    // f(x) = r^2arccos((r - h)/r)-(r-h)sqrt(2rh - h^2) - A
    // f'(x) = sqrt(2rh - h^2) - (((r-h)^2)/(sqrt(2rh-h^2))) + (r / (sqrt(1 - (((r - h)^2)/(r^2)))))

    loop {
        x1 = x0 -
            ((radius.powi(2) * ((radius - x0) / radius).acos() - ((radius - x0) * ((2.0 * radius * x0) - (x0.powi(2))).sqrt()) - area) /
            (((2.0 * radius * x0) - (x0.powi(2))).sqrt() - (((radius - x0).powi(2)) / (((2.0 * radius * x0) - (x0.powi(2))).sqrt())) + (radius / ((1.0 - (((radius - x0).powi(2)) / (radius.powi(2)))).sqrt()))));

        if (x1 - x0).abs() < max_difference {
            return x1
        } else {
            x0 = x1;
        }
    }
}

fn len_of_number(mut n: i128) -> i128 {
    let mut result: i128 = 0;
    while n != 0 {
        result += 1;
        n /= 10;
    }
    result
}