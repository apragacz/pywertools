from itertools import izip, tee


def offset_iter(iterable, offset=0):
    it = iter(iterable)
    for _ in range(offset):
        it.next()
    return it


def limit_iter(iterable, limit):
    for i, elem in enumerate(iterable):
        if limit <= i:
            return
        yield elem


def arithmethic_progression(iterable, a=1, b=0):
    b_a = b % a
    for i, elem in enumerate(iterable):
        if i >= b and i % a == b_a:
            yield elem


def consecutive(iterable, n=2, step=1):
    tee_iters = tee(iterable, n)
    iters = [arithmethic_progression(it, step, step * i)
             for i, it in enumerate(tee_iters)]
    return izip(*iters)
