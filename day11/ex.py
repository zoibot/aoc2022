modulus = 13 * 17 * 19 * 23

monkeys = [
    {
        'starting': [79, 98],
        'op': lambda old: old * 19,
        'test': (lambda x: x%23 == 0, 2, 3),
    },
    {
        'starting': [54, 65, 75, 74],
        'op': lambda old: old + 6,
        'test': (lambda x: x%19 == 0, 2, 0),
    },
    {
        'starting': [79, 60, 97],
        'op': lambda old: old * old,
        'test': (lambda x: x%13 == 0, 1, 3),
    },
    {
        'starting': [74],
        'op': lambda old: old + 3,
        'test': (lambda x: x%17 == 0, 0, 1),
    },
]