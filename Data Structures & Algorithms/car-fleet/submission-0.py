class Solution:
    def will_overtake(self, car1: tuple[int, int], car2: tuple[int, int], target: int) -> bool:
        return ((target - car2[0]) / car2[1]) < ((target - car1[0]) / car1[1] + 1e-15)


    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car_list = sorted(zip(position, speed), key=lambda x: x[0])
        fleets = 1
        fleet_leader = car_list.pop()
        while car_list:
            new_car = car_list.pop()
            if not self.will_overtake(fleet_leader, new_car, target):
                fleets += 1
                fleet_leader = new_car

        return fleets