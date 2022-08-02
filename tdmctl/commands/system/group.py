import typer
from rich.console import Console
from rich.table import Table
from rich import print

from tdmctl.core import Api

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
    api = Api()
    groups_json = api.get("/group/").json()
    table = Table("Id", "Name")
    for group in groups_json["results"]:
        table.add_row(str(group.get("id")), group.get("name"))
    console.print(table)


@app.command(name="create")
def create_command(name: str):
    """
    Create a new group
    """
    api = Api()
    reply = api.post("/group/", {"name": name})
    if reply.status_code == 201:
        print("Group {} created with id {}".format(name, reply.json().get("id")))
    elif reply.status_code == 400:
        print("Bad request : {}".format(reply.json().get("name")))
    else:
        print("Not handled : {}".format(reply.text))


@app.command(name="delete")
def delete_command(id: str):
    """
    Delete a group
    """
    api = Api()
    reply = api.delete("/group/{}/".format(id))
    if reply.status_code == 204:
        print("Group {} deleted".format(id))
    elif reply.status_code == 404:
        print("Group {} not found".format(id))
    else:
        print("Not handled : {}".format(reply.text))
