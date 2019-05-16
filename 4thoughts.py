#https://open.kattis.com/problems/4thought

def combination(n):
    signs = ['*', '+', '-', '//']

    for i in signs:
        for j in signs:
            for k in signs:
                solution = '4 '+i+' 4 '+j+' 4 '+k+' 4'
                if int(eval(solution)) == int(n):
                    if '//' in solution:
                        solution = solution.replace('//', '/')
                    return solution + ' = ' + n

loops = int(input())

for i in range(loops):
    n = input()
    if combination(n) is None:
        print("no solution")
    else:
        print(combination(n))
