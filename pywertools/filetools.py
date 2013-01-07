def content_of_filename(filename, default=None):
    try:
        with open(filename, 'rt') as f:
            return f.read().strip()
    except IOError:
        return None


def set_filename_content(filename, content):
    with open(filename, 'wt') as f:
        f.write(content)
