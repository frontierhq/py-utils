from py_utils.get_azure_short_region import get_azure_short_region


def get_terraform_azurerm_backend_config(
    region: str,
    environment: str,
    zone: str,
) -> tuple[str, str]:
    short_region = get_azure_short_region(region=region)

    resource_group_name = f"rg-{zone}-{environment}-{short_region}-tfstate"
    storage_account_name = f"sa0{zone}0{environment}0{short_region}0tfstate"

    return resource_group_name, storage_account_name


def _test():
    raise NotImplementedError


if __name__ == "__main__":
    _test()
