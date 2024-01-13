import Scratch as tb
import random

if __name__ == '__main__':
    points = []
    for _ in range(20):
        position = (random.randint(200, 800), random.randint(200, 800))
        weight = random.randint(10, 100)
        point = tb.Point(position, weight)
        points.append(point)

    trucks = []
    for _ in range(3):
        truck = tb.Truck(1000)
        trucks.append(truck)

    manager = tb.Manager(points, trucks)
    distance_table = manager.distance_table(points)
    print(distance_table)
    manager.initial_solution(distance_table)