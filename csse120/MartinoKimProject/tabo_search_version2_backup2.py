import math, random, cv2
import copy

class Point:
    num = 0
    def __init__(self, position, weight):
        self.position = position
        self.weight = weight
        self.num = Point.num
        Point.num += 1

    def __repr__(self):
        return "Position{0}".format(self.num)

    def __lt__(self, other):
        return self.num < other.num

    def __eq__(self, other):
        return self.num == other.num

    def distanceTo(self, other):
        del_x = self.position[0] - other.position[0]
        del_y = self.position[1] - other.position[1]
        return math.sqrt(del_x ** 2 + del_y ** 2)

    def __hash__(self):
        return hash(self.num)

class Truck:
    num = 0
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_load = 0
        self.delivery_points = []
        self.num = Truck.num
        Truck.num += 1

    def __repr__(self):
        return "Truck{0} : max_cap = {1}, current_load = {2}, empty space: {3}, points = {4}".format(
            self.num, self.max_capacity, self.current_load, self.max_capacity - self.current_load, self.delivery_points
        )

    def arrange_route(self, route):
        arranged = copy.deepcopy(route)
        while arranged[0].num != -1:
            index = 0
            first = arranged[0]
            arranged = arranged[1:]
            arranged.append(first)
            index += 1
            if index > 5*len(route):
                print(route)
                print("warehouse disappeared")
                return
        return arranged

    def create_route(self, ware_house):
        route = copy.deepcopy(self.delivery_points)
        #route.insert(0, ware_house)
        return route

    def mutate_route(self, route, i, j):
        mutated_route = list(copy.deepcopy(route))
        mutated_route[i], mutated_route[j] = mutated_route[j], mutated_route[i]
        return mutated_route

    def create_mutated_route_dict(self, route, tabo_list):
        mutated_routes = []
        tabos = []
        for i in range(1, len(route)):
            for j in range(i+1, len(route)):
                mutated = self.mutate_route(route, i, j)
                tabo = sorted([mutated[i], mutated[j]])
                if tabo not in tabo_list:
                    mutated_routes.append(tuple(mutated))
                    tabos.append(tabo)
        mutated_route_dict = dict(zip(mutated_routes, tabos))
        return mutated_route_dict

    def find_route_distance(self, route, distance_table):
        distance = 0

        for i in range(1, len(route)):
            distance += distance_table[route[i]][route[i-1]]
        return distance

    def find_best_route(self, mutated_route_dict, distance_table):
        shortest_distance = float('inf')
        best_route = self.delivery_points
        tabo = ()
        for route in mutated_route_dict:
            distance = self.find_route_distance(route, distance_table)
            if shortest_distance > distance:
                shortest_distance = distance
                best_route = route
                tabo = mutated_route_dict[best_route]

        return (best_route, tabo, shortest_distance)

    def tabo_search(self, ware_house, distance_table, trials = 500):
        tabo_list = list()
        local_best_route = best_route = self.create_route(ware_house)
        num_neighbors = len(best_route) * (len(best_route)-1) / 2
        local_best_distance = best_distance = self.find_route_distance(best_route, distance_table)
        tabo_size = num_neighbors/2

        painter = Painter()
        painter.draw_points(self.delivery_points)


        for i in range(trials):
            mutated_routes_dict = self.create_mutated_route_dict(local_best_route, tabo_list)
            num_neighbors = len(mutated_routes_dict)
            local_best = self.find_best_route(mutated_routes_dict, distance_table)
            local_best_route = local_best[0]
            tabo_for_local_best = local_best[1]
            local_best_distance = local_best[2]
            if i % 20 == 0:
                tabo_size = random.randint(int(num_neighbors/2), num_neighbors)

            painter.draw_route(self, local_best_route, i)

            if tabo_for_local_best not in tabo_list:
                tabo_list.append(tabo_for_local_best)
            if len(tabo_list) > tabo_size:
                del tabo_list[0]
            if best_distance >= local_best_distance:
                best_route = local_best_route
                best_distance = local_best_distance

        painter.draw_route(self, best_route, 0)
        cv2.waitKey(0)
        return best_route, best_distance

class Manager:
    def __init__(self, ware_house):
        self.points = []
        self.trucks = []
        self.ware_house = ware_house

    def __repr__(self):
        return "Points : {0}, trucks : {1}".format(self.points, self.trucks)

    def add_point(self, point):
        self.points.append(point)

    def add_ware_house(self, ware_house):
        for truck in self.trucks:
            if ware_house not in truck.delivery_points:
                truck.delivery_points.insert(0, ware_house)

    def del_point(self, point):
        try:
            self.points.remove(point)
        except:
            print("Point does not exist")

    def add_truck(self, truck):
        self.trucks.append(truck)

    def delete_truck(self, truck):
        try:
            self.trucks.remove(truck)
        except:
            print("truck does not exist")

    def distribute_loads(self):

        loads = copy.deepcopy(self.points)
        loads_loaded = []
        for truck in self.trucks:
            for load in loads:
                if truck.current_load + load.weight < truck.max_capacity and truck.num != -1:
                    truck.current_load += load.weight
                    truck.delivery_points.append(load)
                    loads_loaded.append(load)
            loads = [load for load in loads if load not in loads_loaded]
        left_loads = loads

        while len(left_loads) != 0:
            truck = Truck(1000)
            self.add_truck(truck)
            self.add_ware_house(self.ware_house)
            loads_loaded = []
            for load in left_loads:
                if truck.current_load + load.weight < truck.max_capacity and truck.num != -1:
                    truck.current_load += load.weight
                    truck.delivery_points.append(load)
                    loads_loaded.append(load)
            left_loads = [load for load in left_loads if load not in loads_loaded]

        return left_loads


    def create_distance_table(self):
        points = copy.deepcopy(self.points)
        distance_table = {}
        points.insert(0, self.ware_house)
        for p1 in points:
            distances = {}
            for p2 in points:
                distances[p2] = p1.distanceTo(p2)
            distance_table[p1] = distances
        return distance_table

class Painter:
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    def __init__(self):
        self.map = cv2.imread('map.jpg')

    def draw_points(self, points):
        for point in points:
            if Point.num == -1:
                circle_color = Painter.GREEN
            else:
                circle_color = Painter.RED
            cv2.circle(self.map, center = point.position, radius = 5,
                        color = circle_color, thickness=  -1, lineType = cv2.LINE_AA)
            cv2.putText(self.map, org=point.position, text=str(point.num),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0,
                        thickness=1, lineType=cv2.LINE_AA)


    def draw_route(self, truck, route, cur_trial):
        map = self.map.copy()
        for i in range(1, len(route)):
            p1 = route[i].position
            p2 = route[i-1].position
            line_color = (255/5 * truck.num, 0, 255)
            cv2.line(
                map,
                pt1 = p1,
                pt2 = p2,
                color = line_color,
                thickness = 2,
                lineType = cv2.LINE_AA
            )
        cv2.putText(map, org=(10, 25), text='Tabo Trial: %d' % (cur_trial),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0, thickness=1,
                    lineType=cv2.LINE_AA)
        cv2.putText(map, org=(10, 50), text='Truck : %d' % (truck.num),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=0, thickness=1,
                    lineType=cv2.LINE_AA)
        cv2.imshow('map', map)
        cv2.waitKey(1)
