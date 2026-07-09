class Solution:
    def _check_course_neighbors(self, course_map: dict[int, list[int]], course: int, current_courses: set[int]) -> bool:
        if course in current_courses:
            return False

        for neighbor in course_map[course]:
            if not self._check_course_neighbors(course_map, neighbor, current_courses | {course}):
                return False

        course_map[course] = []

        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_map = {i: [] for i in range(numCourses)}

        for course_a, course_b in prerequisites:
            course_map[course_a].append(course_b)

        safe_courses = set()

        for course in course_map.keys():
            if course in safe_courses:
                continue
            current_courses = set()
            if not self._check_course_neighbors(course_map, course, current_courses):
                return False
            safe_courses |= current_courses

        return True