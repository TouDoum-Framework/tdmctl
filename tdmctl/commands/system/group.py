import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.callback()
def callback():
    """
    Manage Group of TouDoum Server
    """


@app.command(name="list")
def list_command():
    """
    Print available group
    """
    pass