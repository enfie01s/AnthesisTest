class PointFinder:
    def __init__(self, periods_in, points_in):
        self.start = 0
        self.end = 0
        self.points = []
        self.point_count = 0
        self.periods_in = periods_in
        self.points_in = points_in
    def parse_data(self, index):
        self.start = self.periods_in[index*2]
        self.end = self.periods_in[index*2+1]
        self.points = list(filter(lambda point: point if point in range(self.start, self.end) else None, self.points_in))
        self.point_count = len(self.points)
        return {
            'start': self.start,
            'end': self.end,
            'points': self.points,
            'point_count': self.point_count
        }
    @property
    def point_count(self):  # Not sure about getting this into an instance just yet
        return self.point_count
    def get_data(self):
        for i,n in enumerate(self.periods_in[::2]):
            Instance = self.parse_data(i)
            print(Instance['start'])
            print(Instance['end'])
            print(Instance['points'])
            print(Instance['point_count'])


results = PointFinder(\
    [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50],\
    [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]\
)
results.get_data()
