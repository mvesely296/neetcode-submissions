import heapq
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass(order=True)
class Process:
    remaining_uses: int
    cooldown: int = field(compare=False, default=0)
    name: str = field(compare=False, default="")


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        process_map: defaultdict[str, int] = defaultdict(lambda: 0)

        for task in tasks:
            process_map[task] -= 1

        processes: list[Process] = []
        cooling_down = []

        for task_name, task_count in process_map.items():
            processes.append(Process(task_count, 0, task_name))

        heapq.heapify(processes)

        iterations = 0
        while processes or cooling_down:
            iterations += 1
            to_remove = []

            for process in cooling_down:
                process.cooldown -= 1
                # print(f"Iter {iterations}: Cooling down process {process.name} to {process.cooldown}")
                if process.cooldown == 0:
                    heapq.heappush(processes, process)
                    to_remove.append(process)

            for process in to_remove:
                cooling_down.remove(process)

            if processes:
                current_process: Process = heapq.heappop(processes)
                current_process.remaining_uses += 1
                # print(f"Iter {iterations}: Running process {current_process.name}.")
                if current_process.remaining_uses < 0:
                    current_process.cooldown = n + 1
                    cooling_down.append(current_process)

            else:
                # print(f"Iter {iterations}: Sitting idle.")
                pass

        return iterations
