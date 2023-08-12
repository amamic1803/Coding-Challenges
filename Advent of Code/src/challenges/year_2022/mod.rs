use crate::challenges::Year;

mod day_01;
mod day_02;
mod day_03;
mod day_04;
mod day_05;
mod day_06;
mod day_07;
mod day_08;
mod day_09;
mod day_10;
mod day_11;
mod day_12;

use day_01::day_01;
use day_02::day_02;
use day_03::day_03;
use day_04::day_04;
use day_05::day_05;
use day_06::day_06;
use day_07::day_07;
use day_08::day_08;
use day_09::day_09;
use day_10::day_10;
use day_11::day_11;
use day_12::day_12;


pub(crate) fn year_2022() -> Year {
    Year::new(
        2022,
        [
            Some(day_01()),
            Some(day_02()),
            Some(day_03()),
            Some(day_04()),
            Some(day_05()),
            Some(day_06()),
            Some(day_07()),
            Some(day_08()),
            Some(day_09()),
            Some(day_10()),
            Some(day_11()),
            Some(day_12()),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
    )
}