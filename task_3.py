def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson_range = range(lesson[0], lesson[1]+1)
    pupil_ranges = make_ranges(pupil)
    tutor_ranges = make_ranges(tutor)
    intervals_list = []
    check_list = []
    check_list += lesson
    check_list += pupil
    check_list += tutor
    for timestump in check_list:
        if timestump in lesson_range:
            pupil_result = check_in_range(timestump, pupil_ranges)
            tutor_result = check_in_range(timestump, tutor_ranges)
            if pupil_result is True and tutor_result is True:
                intervals_list.append(timestump)
    intervals_list.sort()
    time = 0
    for i in range(1, len(intervals_list), 2):
        delta = intervals_list[i] - intervals_list[i-1]
        time += delta
    return time


def check_in_range(timestump, ranges):
    for timedelta in ranges:
        if timestump in timedelta:
            return True      


def make_ranges(intervals):
    range_list = []
    for i in range(1, len(intervals), 2):
        range_list.append(range(intervals[i-1], intervals[i]+1))
    return range_list


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390,
                        1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

for i, test in enumerate(tests):
    test_answer = appearance(test['data'])
    print(test_answer)
    assert test_answer == test['answer'], \
        f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
