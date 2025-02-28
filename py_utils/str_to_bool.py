def str_to_bool(input: str, allow_empty: bool = False) -> bool:
    true_values = {"yes", "true", "t", "1", "y"}
    false_values = {"no", "false", "f", "0", "n"}

    input_lower = input.lower()

    if input_lower in true_values:
        return True
    elif (input_lower in false_values) or allow_empty:
        return False
    else:
        raise ValueError(f"Cannot convert {input_lower} to bool")


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
