import tomllib
import os


def get_project_metadata():
    with open(os.path.join(os.getcwd(), "pyproject.toml"), "rb") as f:
        data = tomllib.load(f)

    return data


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
