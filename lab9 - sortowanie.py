def babelkowe(tab):
    n = len(tab)
    while n > 1:
        for j in range(n - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
        n -= 1
    return tab

def wybieranie(tab):
    n = len(tab)
    imin = 0
    for k in range(n - 1):
        for x in range(k, n):
            if tab[imin] > tab[x]:
                imin = x
        if imin != k:
            tab[k], tab[imin] = tab[imin], tab[k]
        imin = k + 1
    return tab

def wstawianie(tab):
    n = len(tab)
    m = 0
    for k in range(1, n):
        key = tab[k]
        for i in range(k):
            if tab[i] > key:
                m = i
                break
            if i == k-1:
                m = k
        if m == k:
            continue

        for i in range(k, -1, -1):
            if i == m:
                break
            tab[i] = tab[i - 1]

        tab[m] = key
    return tab


tab0 = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
tab1 = [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
tab2 = [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
tab3 = [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
tab4 = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
tab5 = [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]
tab6 = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
tab7 = [4, 5, 2, 7, 0, 9, 1, 3, 6, 8]
tab8 = [0, 8, 2, 7, 6, 3, 9, 1, 5, 4]
tab9 = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]


assert babelkowe(tab0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab3) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab3) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab3) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab4) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab4) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab4) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab6) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab6) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab6) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab7) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab7) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab7) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab8) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab8) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab8) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert babelkowe(tab9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wybieranie(tab9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert wstawianie(tab9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

