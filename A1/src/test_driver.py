## @file test_driver.py
#  @author ?
#  @brief ?
#  @date ?

from date_adt import DateT
from pos_adt import GPosT



def testdates():
    d1 = DateT(1, 1, 2020)
    d2 = DateT(31, 12, 1500)
    d3 = DateT(25, 4, 1764)
    d4 = DateT(6, 10, 787)
    d5 = DateT(29, 11, 1999)
    d6 = DateT(28, 2, 2220)
    testd()


def testd():
    assert testdates().d1.day() == 1
    assert testdates().d2.day() == 31
    assert testdates().d3.day() == 25
    assert testdates().d4.day() == 6
    assert testdates().d5.day() == 29
    assert testdates().d6.day() == 28


def testm():
    assert testdates().d1.month() == 1
    assert testdates().d2.month() == 12
    assert testdates().d3.month() == 4
    assert testdates().d4.month() == 10
    assert testdates().d5.month() == 11
    assert testdates().d6.month() == 2


def testy():
    assert testdates().d1.year() == 2020
    assert testdates().d2.year() == 1500
    assert testdates().d3.year() == 1764
    assert testdates().d4.year() == 787
    assert testdates().d5.year() == 1999
    assert testdates().d6.year() == 2220
