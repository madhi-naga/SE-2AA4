## @file test_driver.py
#  @author ?
#  @brief ?
#  @date ?

import unittest
from date_adt import DateT
from pos_adt import GPosT

d1 = DateT(1, 1, 2020)
d11 = DateT(1, 1, 2021)
d2 = DateT(31, 12, 1500)
d3 = DateT(25, 4, 1764)
d4 = DateT(6, 10, 787)
d44 = DateT(6, 10, 787)
d5 = DateT(29, 11, 1999)
d6 = DateT(28, 2, 2220)

p1 = GPosT(43.5, 79.1)
p2 = GPosT(43.5, 79.1)
p3 = GPosT(43.5, 79.1)
p4 = GPosT(43.5, 79.1)


class TestT(unittest.TestCase):

    def main(self):
        self.test_days()
        self.test_months()
        self.test_years()
        self.test_prev()
        self.test_next()

    def test_days(self):
        self.assertEqual(d1.day(), 1)

        assert d1.day() == 1
        assert d2.day() == 31
        assert d3.day() == 25
        assert d4.day() == 6

    def test_months(self):
        assert d1.month() == 1
        assert d2.month() == 12
        assert d3.month() == 4
        assert d4.month() == 10

    def test_years(self):
        assert d1.year() == 2020
        assert d2.year() == 1500
        assert d3.year() == 1764
        assert d4.year() == 787

    def test_next(self):
        assert d2.next().month() == 1
        assert d2.next().day() == 1
        assert d2.next().year() == 1501
        assert d4.next().month() == 10
        assert d4.next().day() == 7
        assert d4.next().year() == 787

    def test_prev(self):
        assert d1.prev().month() == 12
        assert d1.prev().day() == 31
        assert d1.prev().year() == 2019
        assert d4.prev().month() == 10
        assert d4.prev().day() == 5
        assert d4.prev().year() == 787

    def test_after(self):
        assert d1.after(d2) == True
        assert d1.after(d3) == True
        assert d2.after(d3) == False
        assert d2.after(d4) == True

    def test_before(self):
        assert d1.before(d2) == False
        assert d4.before(d1) == True
        assert d3.before(d1) == True
        assert d3.before(d4) == False

    def test_equal(self):
        assert d1.equal(d2) == False
        assert d4.equal(d44) == True

    def test_add_days(self):
        assert d2.add_days(7).month() == 1
        assert d2.add_days(7).day() == 7
        assert d2.add_days(7).year() == 1501
        assert d1.add_days(30).month() == 1
        assert d1.add_days(30).day() == 31
        assert d1.add_days(30).year() == 2020
        assert d4.add_days(3650).month() == 10
        assert d4.add_days(3650).day() == 6
        assert d4.add_days(3650).year() == 797

    def test_days_between(self):
        assert d1.days_between(d11) == 365

    def test_lat(self):
        pass

    def test_long(self):
        pass

    def test_west_of(self):
        pass

    def test_north_of(self):
        pass

    def test_equal(self):
        pass

    def test_move(self):
        pass

    def test_distance(self):
        pass

    def test_arrival_date(self):
        pass

if __name__ == "__main__":
    unittest.main()
