import typer

from tdmctl.__init__ import __version__
from tdmctl.core import *
from tdmctl.commands import config
app = typer.Typer()

app.add_typer(config.app, name="config")

config.init_home_user_config()


@app.callback()
def callback():
    """
    tdmctl
    """

@app.command()
def version():
    """
    Print the version 
    """
    typer.echo("tdmctl version {}".format(__version__))
