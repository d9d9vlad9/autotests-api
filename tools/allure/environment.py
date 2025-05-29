from config import settings
import platform
import sys


def create_allure_environment_file():
    item = [f'{key}={value}' for key, value in settings.model_dump().items()]
    item.append(f'os_info={platform.system()}, {platform.release()}')
    item.append(f'python_version={sys.version}')
    properties = '\n'.join(item)

    with open(settings.allure_results_dir.joinpath('environment.properties'), "w+") as file:
        file.write(properties)