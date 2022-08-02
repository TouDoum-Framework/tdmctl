import typer

from tdmctl import commands, __version__

app = typer.Typer()

app.add_typer(commands.context_app, name="context")
app.add_typer(commands.system_app, name="system")


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
