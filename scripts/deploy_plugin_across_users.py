import argparse
import io
import logging
import shutil
import tempfile
import zipfile
from collections import namedtuple
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

PLUGINS_DIR = r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins"  # noqa
PLUGIN_URL = r"https://github.com/threedi/hhnk-threedi-plugin/releases/latest/download/hhnk_threedi_plugin.zip"  # noqa

StoredFile = namedtuple("StoredFile", ["path", "content"])


def main():
    args = get_args()
    deploy(
        admin_user=args.admin_user,
        plugins=args.plugin,
        plugins_dir=args.plugins_dir,
        users=args.user,
        users_ignored=args.ignore_user,
        files_ignored=args.ignore_file,
    )


def get_plugin_from_url(admin_plugin_dir, plugin_url=PLUGIN_URL):
    """get a plugin from an url"""
    response = requests.get(plugin_url)
    if response.status_code == 200:
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall(admin_plugin_dir)


def get_users(user_dir="c://Users"):
    """
    Get all directory names (=users) in the Windows user_dir

    Args:
        user_dir (str, optional): Windows user directory. Defaults to "c://Users".

    Returns:
        list: List of users

    """  # noqa
    return [i.name for i in Path(user_dir).glob("*/")]


def read_ignored_files(user_plugin_dir, files_ignored):
    stored_files = []
    for file in files_ignored:
        path = user_plugin_dir.joinpath(file)
        if path.exists():
            print(f"  reading original: {path}")
            stored_files.append(StoredFile(path, path.read_text()))
    return stored_files


def write_ignored_files(stored_files):
    for stored_file in stored_files:
        print(f"  writing original: {stored_file.path}")
        stored_file.path.write_text(stored_file.content)


def copy_directory_content(admin_plugin_dir, user_plugin_dir, files_ignored):
    """Copy directory content, ingnoring some files."""
    user_plugin_dir.mkdir(parents=True, exist_ok=True)

    for path in admin_plugin_dir.glob("*"):
        if path.is_dir():
            if path.name != "external-dependencies":
                shutil.copytree(path, user_plugin_dir.joinpath(path.name))
        elif path.is_file():
            if path.name not in files_ignored:
                shutil.copy(path, user_plugin_dir.joinpath(path.name))


def copy_plugin(admin_plugin_dir, user_plugin_dir, files_ignored):
    # some files we wish to keep
    stored_files = read_ignored_files(user_plugin_dir, files_ignored)

    if user_plugin_dir.exists():
        try:
            print(f"  removing directory: {user_plugin_dir}")
            shutil.rmtree(user_plugin_dir)
        except PermissionError as e:
            logger.error(f"  removing {user_plugin_dir} failed with error: {e}")

            write_ignored_files(stored_files)
            raise e
    print(f"  copying '{admin_plugin_dir}' to {user_plugin_dir}")
    copy_directory_content(admin_plugin_dir, user_plugin_dir, files_ignored)

    # write stored files
    write_ignored_files(stored_files)


def deploy(
    admin_user: str = None,
    plugins: list = ["hhnk_threedi_plugin", "threedi_results_analysis"],
    plugins_dir: str = PLUGINS_DIR,
    users: list = None,
    users_ignored: list = [],
    files_ignored: list = [],
):
    admin_plugins_dir = Path(plugins_dir.format(user=admin_user))

    # get plugin from repository if admin_dir is not specified
    if admin_user is None:
        print(f"no adin_user specified, we will deploy only the hhnk_threedi_plugin from {PLUGIN_URL}")  # noqa
        temp_dir = tempfile.TemporaryDirectory()
        admin_plugins_dir = Path(temp_dir.name)
        get_plugin_from_url(admin_plugins_dir)

    # check what can be copied from admin
    if not admin_plugins_dir.is_dir():
        raise FileNotFoundError(f"""
            {admin_plugins_dir} is not an existing directory
            please evaluate input provided for
            admin_user: '{admin_user}' and plugins_dir: '{plugins_dir}'
            """)
    else:
        for plugin in plugins:
            if not admin_plugins_dir.joinpath(plugin).is_dir():
                logger.warning(
                    f"""
                    plugin '{plugin}' not installed in {admin_plugins_dir}"
                    and cannot be copied.
                    """
                )
        print(f"plugins that can be copied: {plugins}")

    # get users
    if users in [None, [], [""]]:
        users = get_users()

    # copy plugins
    users = [i for i in users if i not in users_ignored + [admin_user]]

    selected_users = []
    for user in users:
        if Path(plugins_dir.format(user=user)).parent.is_dir():
            selected_users.append(user)
    cont = input(f"Deploy to these users: {selected_users}? [y/n]")

    if cont == "y":
        for user in selected_users:
            # print(f"checking user '{user}'")
            user_plugins_dir = Path(plugins_dir.format(user=user))
            if user_plugins_dir.parent.is_dir():
                print(f"  copying plugins to {user_plugins_dir}")
                user_plugins_dir.mkdir(exist_ok=True)
                for plugin in plugins:
                    print(f"  copying plugin: {plugin}")
                    user_plugin_dir = user_plugins_dir / plugin
                    admin_plugin_dir = admin_plugins_dir.joinpath(plugin)
                    # copy plugin
                    copy_plugin(admin_plugin_dir, user_plugin_dir, files_ignored)

            else:
                print(f"user has no plugins-dir: {user_plugins_dir}")


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deploy HHNK QGIS plugins")
    parser.add_argument(
        "--admin_user",
        help="Admin user to copy plugins from. If ignored, the hhnk_threedi_plugin will be copied from the repository",  # noqa
        type=str,
        default=None,
    )
    parser.add_argument(
        "--plugin",
        help="one or more plugins copy",
        action="append",
        default=["hhnk_threedi_plugin"],
    )
    parser.add_argument(
        "--plugins_dir",
        help="plugin directory template. Note, {user} as user-replacement fields (see default by example)",  # noqa
        type=str,
        default=r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins",  # noqa
    )

    parser.add_argument(
        "--user",
        help="one or more users. If non supplied, the list will be populated from c://users",  # noqa
        action="append",
        default=None,
    )

    parser.add_argument(
        "--ignore_user",
        help="one or more users to ignore. If non supplied, the list will be empty",  # noqa
        action="append",
        default=[],
    )

    parser.add_argument(
        "--ignore_file",
        help="list of files that will not be replaced by if found",
        action="append",
        default=["local_settings.py", "api_key.txt"],
    )
    parser.add_argument(
        "--log_level",
        help="Log level (default: INFO)",
        default="INFO",
    )

    args = parser.parse_args()
    logger.setLevel(args.log_level)
    return args


if __name__ == "__main__":
    main()
