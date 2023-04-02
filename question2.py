import unittest
from question1.py import PointFinder

class DataPoints(unittest.TestCase):
    def setUp(self):
        periods = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]
        points = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]
        results = PointFinder(periods, points)

    def test_periods_and_points_are_whole_numbers(self):
        for i,period in enumerate(self.periods[::2]):
            result = results.parse_data(i)
            self.assertTrue(result['start'].is_integer())
            self.assertTrue(result['end'].is_integer())
            for point in result['points']:
                self.assertTrue(point.is_integer())

    def test_list_has_maximum_of_10_periods(self):
        self.assertTrue(periods / 2 <= 10)

    def test_period_under_10_seconds(self):
        for i,period in enumerate(self.periods[::2]):
            result = results.parse_data(i)
            self.assertTrue(result['end'] - result['start'] < 10)

    def test_points_between_1_and_10(self):
        for i,period in enumerate(self.periods[::2]):
            result = results.parse_data(i)
            self.assertTrue(result.point_count > 0 && result.point_count < 10)

    def test_points_in_time_order_asc(self):
        for i,period in enumerate(self.periods[::2]):
            result = results.parse_data(i)
            lastpoint = 0
            for point in result['points']:
                self.assertTrue(point > lastpoint)
                lastpoint = point


if __name__ == '__main__':
    unittest.main()

"""
All periods and data points must be whole numbers = pass

There can only ever be a maximum of 10 periods = pass

Each point represents one second - a period may be no longer than 10 seconds = fail (one of the periods is 26, 40 which is longer than 10 seconds)

Each period must contain between one and 10 data points = pass

Points must be stored in time order, with the earliest listed first = fail (example output for one of the periods is [24, 24, 21, 22] which is not in order)
"""
