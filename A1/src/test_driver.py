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
d22 = DateT(1, 2, 1501)
d3 = DateT(25, 4, 1764)
d4 = DateT(6, 10, 787)
d44 = DateT(6, 10, 787)
d5 = DateT(29, 11, 1999)
d6 = DateT(28, 2, 2220)

p1 = GPosT(43.5, 79.1)
p2 = GPosT(-12.357, -169.599)
p22 = GPosT(-12.357, -169.599)
p3 = GPosT(83.3, -12.47)
p4 = GPosT(23.77, 99.521)


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
        assert d4.add_days(3653).month() == 10
        assert d4.add_days(3653).day() == 6
        assert d4.add_days(3653).year() == 797

    def test_days_between(self):
        assert d1.days_between(d11) == 366
        assert d2.days_between(d22) == 32

    def test_lat(self):
        assert p1.lat() == 43.5
        assert p2.lat() == -12.357
        assert p3.lat() == 83.3

    def test_long(self):
        assert p1.long() == 79.1
        assert p2.long() == -169.599
        assert p3.long() == -12.47

    def test_west_of(self):
        assert p1.west_of(p2) == False
        assert p2.west_of(p4) == True
        assert p3.west_of(p1) == True

    def test_north_of(self):
        assert p1.north_of(p2) == True
        assert p3.north_of(p4) == True
        assert p1.north_of(p3) == False

    def test_equal(self):
        assert p2.equal(p22) == True
        assert p1.equal(p3) == False

    def test_move(self):
        p1.move(14.5, 452)
        self.assertAlmostEqual(p1.lat(), 47.4261, delta=0.1)
        self.assertAlmostEqual(p1.long(), 80.603, delta=0.1)
        p2.move(46.5, 985.33)
        self.assertAlmostEqual(p2.lat(), -6.1925, delta=0.1)
        self.assertAlmostEqual(p2.long(), -163.145, delta=0.1)
        p3.move(-33.61, 2673.67)
        self.assertAlmostEqual(p3.lat(), 71.1877, delta=0.1)
        self.assertAlmostEqual(p3.long(), -148.089, delta=0.1)

    def test_distance(self):
        self.assertAlmostEqual(p1.distance(p2), 12660, delta=5)
        self.assertAlmostEqual(p2.distance(p4), 10650, delta=5)
        self.assertAlmostEqual(p3.distance(p1), 5232, delta=5)

    def test_arrival_date(self):
        res = p1.arrival_date(p2, d1, 263)
        self.assertEqual(res.year(), 2020)
        self.assertEqual(res.month(), 2)
        self.assertEqual(res.day(), 18)

        res2 = p4.arrival_date(p3, d5, 1.64)
        self.assertEqual(res2.year(), 2012)
        self.assertEqual(res2.month(), 9)
        self.assertEqual(res2.day(), 11)

        res3 = p2.arrival_date(p3, d4, 17.4)
        self.assertEqual(res3.year(), 789)
        self.assertEqual(res3.month(), 8)
        self.assertEqual(res3.day(), 29)


if __name__ == "__main__":
    unittest.main()
