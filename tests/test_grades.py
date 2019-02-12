from grades import get_grades, get_averages, rank_scores
def test_get_grades():
    grades = get_grades('grades.txt')
    print(grades)
    d = {'bob': [78,58,88], etc.}
    assert grades == d
#    assert 1 == 0  # this will print out prints if test pass

def test_get_averages():
    grades = get_grades('grades.txt')
    avgs = get.averages(grades)
    print(avgs)
    assert 1 == 0
    assert avgs == [('bob'), 85.333  etc.]

def test_rank_scores():
    grades = get_grades('grades.tx')
    avgs = get.averages(grades)
    sorted(avgs, key=lambda x: print(x, type(x)))
    sorted(avgs, key=lambda t: t[1][::-1]) 
    rank = rank_scores(avgs) #sort desc by second element

