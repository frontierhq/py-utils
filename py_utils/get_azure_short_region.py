def get_azure_short_region(region: str) -> str:
    short_region = None
    match region:
        case "uksouth":
            short_region = "uks"
        case "ukwest":
            short_region = "ukw"
        case _:
            raise ValueError(f"unknown region: {region}")
    return short_region


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
