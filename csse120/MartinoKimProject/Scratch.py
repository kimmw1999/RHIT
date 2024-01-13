import math, random, cv2, copy

class Point:
    num = 0
    def __init__(self, position, weight):
        self.position = position
        self.num = Point.num
        Point.num += 1
        self.weight = weight


    def __repr__(self):
        return "Point{0}".format(self.num)
    def __lt__(self, other):
        return self.num < other.num
    def __eq__(self, other):
        return self.num == other.num
    def distanceTo(self, other):
        del_x = self.position[0] - other.position[0]
        del_y = self.position[1] - other.position[1]
        return math.sqrt(del_x**2 + del_y**2)

    def __hash__(self):
        return hash(self.num)

class Truck:
    num = 0
    def __init__(self, capacity):
        self.num = Truck.num
        Truck.num += 1
        self.weight = 0
        self.points = []
        self.capacity = capacity

    def __repr__(self):
        return "Truck{0}".format(self.num)

    def add_point(self, point):
        self.points.append(point)
        self.weight += point.weight

class Manager:
    def __init__(self, points, trucks):
        self.points = points
        self.trucks = trucks

    def distance_table(self, points):
        distance_table = {}
        for point in points:
            for point2 in points:
                table = {}
                if point.num != point2.num:
                    table[point2] = point.distanceTo(point2)
            distance_table[point] = table
        return distance_table

    def initial_solution(self, distance_table):
        def find_nearest_point(self, point, distance_table):
            distance_table = sorted(distance_table[point].items(), key=lambda item: item[1])
            print(distance_table)
            for point2 in distance_table:
                if point2[0] in self.points:
                    print(point2[0])
                    return point2[0]
            print("none")
            return None

        for truck in self.trucks:
            point = self.points[random.randint(0, len(self.points))]
            truck.add_point(point)
            self.points.remove(point)
            next = find_nearest_point(self, point, distance_table)
            while truck.capacity > truck.weight + next.weight or next is None:
                truck.add_point(next)
                self.points.remove(next)
                next = find_nearest_point(self, next, distance_table)






class Painter:
    def __init__(self):
        pass
    def draw_points(self):
        pass
    def draw_route(self):
        pass