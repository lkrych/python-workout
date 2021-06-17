from operator import itemgetter

PEOPLE = [('Joe', 'Biden', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603), ('Boris', 'Johnson', 4.56)]

def format_sort_records(records):
    for r in sorted(records, key=itemgetter(1, 0)):
        print(f'{r[1]:10}{r[0]:10}{r[2]:5.2}')

format_sort_records(PEOPLE)
