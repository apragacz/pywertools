def ilimit(iterable, limit=100, offset=0):
    end_offset = offset + limit
    for i, elem in enumerate(iterable):
        if offset <= i and i < end_offset:
            yield elem
        elif end_offset <= i:
            return
