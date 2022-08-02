import requests

from tdmctl import __version__
from . import ContextManager, Context


class ApiNotContextSetError(Exception):
    pass


class Api:
    context_manager: ContextManager
    context: Context

    endpoint: str
    headers: dict
    credentials: tuple
    user: str
    password: str

    def __init__(self):
        self.context_manager = ContextManager()
        self.context = self.context_manager.current

        if not self.context:
            exit("No context set. Use `tdmctl context set` to set a context.")
            # raise ApiNotContextSetError("Cant build API without context set")

        self.endpoint = self.context.host
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": f"tdmctl/{__version__}",
        }
        self.credentials = (self.context.user, self.context.password)

    def get(self, path: str, page: int = 1, **kwargs) -> requests.Response:
        """
        Make a GET request to the API.
        param path: The path to the resource.
        param page: The page to get.
        param kwargs: Any additional arguments to pass to requests.get.(Note headers and auth are handled internally.)
        """
        return requests.get(f"{self.endpoint}{path}?page={page}", headers=self.headers, auth=self.credentials, **kwargs)

    def post(self, path: str, data: dict, **kwargs) -> requests.Response:
        """
        Make a POST request to the API.
        param path: The path to the resource.
        param data: The data to send.
        param kwargs: Any additional arguments to pass to requests.post.(Note headers and auth are handled internally.)
        """
        return requests.post(f"{self.endpoint}{path}", headers=self.headers, auth=self.credentials, json=data, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        """
        Make a DELETE request to the API.
        param path: The path to the resource.
        param kwargs: Any additional arguments to pass to requests.delete.(Note headers and auth are handled internally.)
        """
        return requests.delete(f"{self.endpoint}{path}", headers=self.headers, auth=self.credentials, **kwargs)
