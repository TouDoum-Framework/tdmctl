import typer

from tdmctl.__init__ import __version__
from tdmctl.commands import context
from tdmctl.commands import system

context.init_home_user_config()

app = typer.Typer()

app.add_typer(context.app, name="context")
app.add_typer(system.app, name="system")


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
