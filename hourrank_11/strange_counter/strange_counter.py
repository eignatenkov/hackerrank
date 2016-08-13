# Bob has a strange counter. At the first second, t = 1, it displays
# the number 3. At each subsequent second, the number displayed by the counter
# decrements by 1.
#
# The counter counts down in cycles. In the second after the counter counts
# down to 1, the number becomes 2x the initial number for that countdown cycle
# and then continues counting down from the new initial number in a new cycle.
# Given a time, t, find and print the value displayed by the counter at time t.
#
# Input Format
#
# A single integer denoting the value of t.

# Example: 3 2 1 6 5 4 3 2 1 12 11 10 9 8 7 ...

# Time intervals are 3, 3*2, 3*2^2, ..., 3*2^k.

# The borders of intervals are: 1 - 3, 2 - 9, 3 - 21, 4 - 45.

# divide by 3: 1, 3, 7, 15 - 2^n_interval - 1.

# true borders - 3*(2^n_interval - 1).

# so, if we have number k, we can divide it by three, add 1 and take log base 2
# for the last number in nth interval it will give us n. It means that if don't
# add 1, take int part, and add 1 to it, we will have real interval number.
# Let's test it.

from math import log
import unittest


def interval_number(time):
    return int(log(time/3 + 1, 2)) if log(time/3 + 1,2).is_integer() else int(log(time/3 + 1, 2)) + 1


def interval_start_number(int_number):
    return 3*(2 ** (int_number - 1))


def interval_start_time(int_number):
    return 1 + 3 * (2 ** (int_number - 1) - 1)


def counter_value(time):
    int_number = interval_number(time)
    int_start = interval_start_number(int_number)
    int_start_time = interval_start_time(int_number)
    return int_start - (time - int_start_time)


class TestIntervalNumber(unittest.TestCase):
    def test_one(self):
        self.assertEqual(interval_number(1), 1)

    def test_three(self):
        self.assertEqual(interval_number(3), 1)

    def test_four(self):
        self.assertEqual(interval_number(4), 2)

    def test_nine(self):
        self.assertEqual(interval_number(9), 2)


class TestIntervalStartNumber(unittest.TestCase):
    def test_one(self):
        self.assertEqual(interval_start_number(1), 3)

    def test_two(self):
        self.assertEqual(interval_start_number(2), 6)


class TestIntervalStartTime(unittest.TestCase):
    def test_one(self):
        self.assertEqual(interval_start_time(1), 1)

    def test_two(self):
        self.assertEqual(interval_start_time(2), 4)

    def test_three(self):
        self.assertEqual(interval_start_time(3), 10)


class TestCounterValue(unittest.TestCase):
    def test_one(self):
        self.assertEqual(counter_value(1), 3)

    def test_three(self):
        self.assertEqual(counter_value(3), 1)

    def test_four(self):
        self.assertEqual(counter_value(4), 6)

    def test_nine(self):
        self.assertEqual(counter_value(9), 1)

    def test_eleven(self):
        self.assertEqual(counter_value(11), 11)

if __name__ == "__main__":
    unittest.main()
