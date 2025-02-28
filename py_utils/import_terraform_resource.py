from python_terraform import Terraform


def import_terraform_resource(
    terraform: Terraform,
    address: str,
    id: str,
    **kwargs: dict,
):
    print(f"importing terraform resource to '{address}'")
    return_code, _, _ = terraform.import_cmd(
        address,
        id,
        capture_output=False,
        **kwargs,
    )
    if return_code != 0 and return_code != 1:
        exit(return_code)


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
