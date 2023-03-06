import argparse
from pathlib import Path
import logging
import shutil

logger = logging.getLogger(__name__)

PLUGINS_DIR = r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins"


def main():
    args = get_args()
    deploy(
        admin_user=args.admin_user,
        plugins=args.plugins,
        plugins_dir=args.plugins_dir,
        users=args.users,
        ignore_files=args.ignore_files,
    )


def get_users(user_dir="c://Users"):
    """
    Get all directory names (=users) in the Windows user_dir

    Args:
        user_dir (str, optional): Windows user directory. Defaults to "c://Users".

    Returns:
        list: List of users

    """
    return [i.name for i in Path(user_dir).glob("*/")]


def deploy(
    admin_user: str,
    plugins: list[str] = ["hhnk_threedi_plugin", "ThreeDiToolbox"],
    plugins_dir: str = PLUGINS_DIR,
    users: list[str] = None,
    ignore_files: list[str] = ["local_settings.py", "api_key.txt"],
):
    admin_plugins_dir = Path(plugins_dir.format(user=admin_user))

    # check what can be copied from admin
    if not admin_plugins_dir.is_dir():
        raise FileNotFoundError(
            f"""
                                {admin_plugins_dir} is not an existing directory
                                please evaluate input provided for
                                admin_user: '{admin_user}' and plugins_dir: '{plugins_dir}'
                                """
        )
    else:
        for plugin in plugins:
            if not admin_plugins_dir.joinpath(plugin).is_dir():
                logger.warning(
                    f"""
                               plugin '{plugin}' not installed in {admin_plugins_dir}"
                               and cannot be copied.
                               """
                )
    # get users
    if users is None:
        users = get_users()

    # copy plugins
    users = [i for i in users if i != admin_user]
    for user in users:
        print(f"checking user '{user}'")
        user_plugins_dir = Path(plugins_dir.format(user=user))
        if user_plugins_dir.is_dir():
            print(f"  copying plugins to {user_plugins_dir}")
            for plugin in plugins:
                print(f"  copying plugin: {plugin}")
                user_plugin_dir = user_plugins_dir / plugin
                keep_files = []
                for file in ignore_files:
                    file_path = user_plugin_dir.joinpath(file)
                    if file_path.exists():
                        print(f"  reading original: {file_path}")
                        keep_files.append((file_path, file_path.read_text()))
                if user_plugin_dir.exists():
                    try:
                        print(f"  removing directory: {user_plugin_dir}")
                        shutil.rmtree(user_plugin_dir)
                    except PermissionError as e:
                        logger.error(
                            f"  removing {user_plugin_dir} failed with error: {e}"
                        )
                        raise e
                print(
                    f"  copying '{admin_plugins_dir.joinpath(plugin)}' to {user_plugin_dir}"
                )
                shutil.copytree(admin_plugins_dir.joinpath(plugin), user_plugin_dir)

                for file, text in keep_files:
                    print(f"  writing original '{file}'")
                    file.write_text(text)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deploy HHNK QGIS plugins")
    parser.add_argument(
        "--admin_user", help="Admin user to copy plugins from", type=str
    )
    parser.add_argument(
        "--plugins",
        help="list of names with plugins to copy",
        type=list,
        default=["hhnk_threedi_plugin", "ThreeDiToolbox"],
    )
    parser.add_argument(
        "--plugins_dir",
        help="plugin directory template. Note, {user} as user-replacement fields (see default by example)",
        type=str,
        default=r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins",
    )

    parser.add_argument(
        "--users",
        help="list of users. If non supplied, the list will be populated from c://users",
        type=list,
        default=None,
    )

    parser.add_argument(
        "--ignore_files",
        help="list of files that will not be replaced by if found",
        type=list,
        default=["local_settings.py", "api_key.txt"],
    )
    parser.add_argument(
        "--log_level",
        help="Log level (default: INFO)",
        default="INFO",
    )

    args = parser.parse_args()
    logger.setLevel(args.log_level)
    if not args.admin_user:
        parser.error("At least --admin_user is to be specified")
    return args

deploy("danie")
# if __name__ == "__main__":
#     main()
