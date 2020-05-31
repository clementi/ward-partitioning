import random
import sys
import time

from sortedcontainers import SortedSet


class Household(object):
    def __init__(self, name, composite, members, likely_members,
                 priests, likely_priests, teachers, likely_teachers,
                 deacons, likely_deacons, elders, likely_elders):
        self.name = name
        self.composite = composite == 'TRUE'
        self.members = int(members)
        self.likely_members = int(likely_members)
        self.priests = int(priests)
        self.likely_priests = int(likely_priests)
        self.teachers = int(teachers)
        self.likely_teachers = int(likely_teachers)
        self.deacons = int(deacons)
        self.likely_deacons = int(likely_deacons)
        self.elders = int(elders)
        self.likely_elders = int(likely_elders)

    def __repr__(self):
        return f"Household(name={self.name}, " \
               f"composite={self.composite}, " \
               f"members={self.likely_members}/{self.members}, " \
               f"priests={self.likely_priests}/{self.priests}, " \
               f"teachers={self.likely_teachers}/{self.teachers}, " \
               f"deacons={self.likely_deacons}/{self.deacons}, " \
               f"elders={self.likely_elders}/{self.elders})"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return not(self == other or self < other)

    def __hash__(self):
        return hash(self.name)


class Group(object):
    def __init__(self, group_id):
        self.group_id = group_id
        self.households = SortedSet()

    def add(self, household):
        self.households.add(household)

    def members(self):
        return self._count(lambda h: h.members)

    def _count(self, selector):
        return sum(map(selector, self.households))

    def likely_members(self):
        return self._count(lambda h: h.likely_members)

    def priests(self):
        return self._count(lambda h: h.priests)

    def likely_priests(self):
        return self._count(lambda h: h.likely_priests)

    def teachers(self):
        return self._count(lambda h: h.teachers)

    def likely_teachers(self):
        return self._count(lambda h: h.likely_teachers)

    def deacons(self):
        return self._count(lambda h: h.deacons)

    def likely_deacons(self):
        return self._count(lambda h: h.likely_deacons)

    def elders(self):
        return self._count(lambda h: h.elders)

    def likely_elders(self):
        return self._count(lambda h: h.likely_elders)

    def __repr__(self):
        return f"Group(group_id={self.group_id}, " \
               f"members={self.likely_members()}/{self.members()}, " \
               f"priests={self.likely_priests()}/{self.priests()}, " \
               f"teachers={self.likely_teachers()}/{self.teachers()}, " \
               f"deacons={self.likely_deacons()}/{self.deacons()}, " \
               f"elders={self.likely_elders()}/{self.elders()})"

    def __hash__(self):
        return hash(self.group_id)

    def __lt__(self, other):
        return self.group_id < other.group_id

    def __eq__(self, other):
        return self.group_id == other.group_id

    def __gt__(self, other):
        return not(self < other or self == other)


def to_household(line):
    parts = list(map(lambda part: part.strip(), line.split(',')))
    return Household(parts[0], parts[1], parts[2], parts[3],
                     parts[4], parts[5], parts[6], parts[7],
                     parts[8], parts[9], parts[10], parts[11])


def main():
    if len(sys.argv) < 2:
        raise Exception("Data file required.")
    households_file_path = sys.argv[1]

    limit = 99 if len(sys.argv) < 3 else int(sys.argv[2])
    seed = int(time.time() * 1000000) if len(sys.argv) < 4 else int(sys.argv[3])

    if seed != 0:
        print(f"Using seed {seed}")
        random.seed(seed)

    print(f"Using limit {limit}")

    with open(households_file_path, "r") as households_file:
        households = list(map(to_household, filter(lambda line: not line.startswith("Name,"), households_file)))

        if seed != 0:
            random.shuffle(households)

        groups = SortedSet()
        current_group = Group(0)
        for household in households:
            if household.members + current_group.members() > limit:
                groups.add(current_group)
                current_group = Group(current_group.group_id + 1)

            current_group.add(household)
        groups.add(current_group)

        for group in groups:
            print(group)

        print(sum(map(lambda g: g.members(), groups)))


if __name__ == "__main__":
    main()
