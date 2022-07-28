from pathlib import Path

import yaml
import typer

from tdmctl import core

#
# Litle logic
#

config = {}

def get_config_path():
    """
    Get the config path
    """
    return core.get_home_user_path() + "/.tdmctl/config.yaml"

def init_home_user_config():
    """
    Initialize the home user config directory
    """
    home_user_config_path = core.get_home_user_path() + "/.tdmctl"
    if not Path(home_user_config_path).exists():
        Path(home_user_config_path).mkdir(parents=True)

def config_exists():
    """
    Check if the config file exists
    """
    home_user_config_path = get_config_path()
    return Path(home_user_config_path).exists()

def get_config():
    """
    Get the config file
    """
    home_user_config_path = get_config_path()
    if not config_exists():
        save_config()
    with open(home_user_config_path, 'r', encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def save_config():
    """
    Save the config file
    """
    home_user_config_path = get_config_path()
    if not config_exists:
        Path(home_user_config_path).touch()
    with open(home_user_config_path, 'w+', encoding="utf-8") as f:
        yaml.dump(config, f)

def print_config():
    """
    Print the config file
    """

    lconfig = get_config()
    typer.echo("Current context: " + lconfig["current_context"])
    typer.echo("Host: " + lconfig["context"][lconfig["current_context"]]["host"])
    typer.echo("User: " + str(lconfig["context"][lconfig["current_context"]]["user"]))
    typer.echo("Pass: [REDACTED]")

#
# Command zone
#
app = typer.Typer()

@app.command()
def show():
    """
    Print the current context with host and username
    """
    if config_exists():
        print_config()
    else:
        typer.echo("No config file found")
        create = typer.confirm("Create a config file?")
        if create:
            config["context"] = {}
            name = typer.prompt("Enter name for context connection (not hostname)")
            config["current_context"] = name
            config["context"][name] = {
                "host": typer.prompt("Enter hostname for server api (without api suffix)"),
                "user": typer.prompt("Enter username"),
                "pass": typer.prompt("Enter password"),
            }
            save_config()
            typer.echo("Config file created")
            print_config()
        else:
            typer.echo("No config file created")