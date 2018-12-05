import datetime


class current_watch:
    def __init__(self):
        self.guard = None
        self.guards_sleep_hours = {}
        self.asleep = 0

    def change_guard(self, guard_str):
        guard_no = int(guard_str.split(" ")[3].strip("#"))
        if not guard_no in self.guards_sleep_hours:
            self.guards_sleep_hours[guard_no] = [0 for _ in range(60)]

        self.guard = guard_no
        self.asleep = 0

    def guard_sleeps(self, sleep_str):
        self.asleep = 1
        self.sleep_start_time = int(sleep_str.split(" ")[1].split(":")[1].strip("]"))

    def guard_wakens(self, wake_str):
        self.asleep = 0
        awaken_time = int(wake_str.split(" ")[1].split(":")[1].strip("]"))
        for i in range(self.sleep_start_time, awaken_time):
            self.guards_sleep_hours[self.guard][i] += 1


def argmax(list_val):
    tip = 0
    tip_idx = 0
    for idx in range(len(list_val)):
        if list_val[idx] > tip:
            tip_idx, tip = idx, list_val[idx]

    return tip_idx, tip


data = open("input.txt").read().split("\n")
data = data[:-1]
dates = [i.split("]")[0].strip("[") for i in data]
dates = [datetime.datetime.strptime(i, "%Y-%m-%d %H:%M") for i in dates]
combined = list(zip(data, dates))
combined_sorted = sorted(combined, key=lambda x: x[1])

guard_state = current_watch()
for i in combined_sorted:
    print(i[0])
    if "Guard" in i[0]:
        guard_state.change_guard(i[0])

    if "asleep" in i[0]:
        guard_state.guard_sleeps(i[0])

    if "wakes" in i[0]:
        guard_state.guard_wakens(i[0])

# Part 1 -
print(
    (lambda x: x[0] * x[1][0])(
        max(
            [(key, argmax(val)) for key, val in guard_state.guards_sleep_hours.items()],
            key=lambda x: x[1][0],
        )
    )
)

# Part 2 -
print(
    (lambda x: x[0] * x[1][0])(
        max(
            [(key, argmax(val)) for key, val in guard_state.guards_sleep_hours.items()],
            key=lambda x: x[1][1],
        )
    )
)
