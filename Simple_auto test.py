from functions import salary, hello_who

assert hello_who('q') == 'hello, q ' 'AAAAAA'
assert hello_who('qq') == 'hello, qq ' 'AAAAAA'
assert hello_who('qqq') == 'hello, qqq ' 'AAAAAA'
assert hello_who('qqqq') == 'hello, qqqq ' 'AAAAAA'
assert salary(hours=2,salary_by_hour=10) == 20, 'AAAAAA'
assert salary(hours=3,salary_by_hour=10) == 30, 'AAAAAA'
assert salary(hours=4,salary_by_hour=10) == 40, 'AAAAAA'