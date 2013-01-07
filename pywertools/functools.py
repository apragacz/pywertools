def compose(*args):
    return reduce(lambda g, f: (lambda elem: f(g(elem))), reversed(args))
