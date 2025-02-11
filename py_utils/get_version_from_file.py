import os


def get_version_from_file():
    with open(os.path.join(os.getcwd(), "VERSION")) as f:
        version = f.readline()
    return version.rstrip()


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
