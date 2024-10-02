# Alias: ОбщегоНазначенияУНФ

from src.internal.module import app_abilities

# Alias: ЭтоУНФ
def is_smb() -> bool:
    """
    Returns True, if the current configuration is Small Business
    :return: True, if the current configuration is Small Business
    """
    return app_abilities.is_smb()

# Alias: ЭтоРозница
def is_retail() -> bool:
    """
    Returns True, if the current configuration is Retail
    :return: True, if the current configuration is Retail
    """
    return app_abilities.is_resident()