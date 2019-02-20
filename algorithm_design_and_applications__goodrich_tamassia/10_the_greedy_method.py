def scheduling(tasks):
    schedule = []
    for task in sorted(tasks):
        for bucket in schedule:
            if bucket[-1][1] <= task[0]:
                bucket.append(task)
                task = None
                break
        if task:
            schedule.append([task])
    return schedule


if __name__ == '__main__':
    print(scheduling({(1, 4), (5, 9), (4, 6), (3, 5)}))
    print(scheduling({(1, 3), (1, 5), (5, 7), (4, 7)}))
    print(scheduling({(1, 3), (1, 4), (2, 5), (3, 7), (4, 7), (6, 9), (7, 8)}))
