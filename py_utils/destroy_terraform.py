from py_utils.apply_terraform import apply_terraform
from python_terraform import IsFlagged, Terraform


def destroy_terraform(
    terraform: Terraform,
    plan_only: bool = False,
    **kwargs: dict,
) -> dict:
    apply_terraform(
        terraform=terraform,
        plan_only=plan_only,
        destroy=IsFlagged,
        **kwargs,
    )


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
