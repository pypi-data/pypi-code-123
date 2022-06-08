class ConfigKey:
    CURRENT_PROGRAM_ID = 'PROGRAM_CURRENT_PROGRAM_ID'
    DEFAULT_OUTPUT_FORMAT = 'DEFAULT_OUTPUT_FORMAT'
    ACCOUNT_EMAIL = 'ACCOUNT_EMAIL'
    ACCOUNT_PASSWORD = 'ACCOUNT_PASSWORD'
    ALI_OSS_ENDPOINT = 'ALI_OSS_ENDPOINT'
    LEBESGUE_ADDRESS = 'LEBESGUE_ADDRESS'
    CONFIG_FILE_DIR = 'CONFIG_FILE_DIR'
    STORAGE_BUCKET_NAME = 'STORAGE_BUCKET_NAME'
    CHECK_VERSION_LEVEL = "CHECK_VERSION_LEVEL"


class GlobalConfig:
    # LEBESGUE_ADDRESS = 'https://test.dp.tech/'
    # LEBESGUE_ADDRESS = 'http://172.16.8.21:8000/'
    LEBESGUE_ADDRESS = 'https://lebesgue.dp.tech/'
    STORAGE_ENDPOINT = 'oss-cn-shenzhen.aliyuncs.com'
    STORAGE_BUCKET_NAME = 'dpcloudserver'
    CONFIG_ACTION_RECORD = 'lbg_action.csv'
    CONFIG_FILE_DIR = '~/.lbg/'
    CONFIG_FILE_NAME = 'lbg_cli_context.json'
    CALLER_NAME = 'lbg'
    CHECK_VERSION_LEVEL = 1
