"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.
    """
    def __init__(self):
        self.children: dict[str, RouteTrieNode] = {}
        self.handler: Optional[str] = None

    def insert(self, part: str) -> None:
        if part not in self.children:
            self.children[part] = RouteTrieNode()

class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.
    """
    def __init__(self, root_handler: str):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: list[str], handler: str) -> None:
        node = self.root
        for part in path_parts:
            node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts: list[str]) -> Optional[str]:
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.
    """
    def __init__(self, root_handler: str, not_found_handler: str):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path: str, handler: str) -> None:
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path: str) -> str:
        path_parts = self.split_path(path)
        if len(path_parts) == 0:
            return self.route_trie.root.handler
        handler = self.route_trie.find(path_parts)
        return handler if handler is not None else self.not_found_handler

    def split_path(self, path: str) -> list[str]:
        return [part for part in path.strip("/").split("/") if part]

if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Test cases
    print(router.lookup(""))                   # root handler
    print(router.lookup("/"))                  # root handler
    print(router.lookup("/home"))              # not found handler
    print(router.lookup("/home/about"))        # about handler
    print(router.lookup("/home/about/"))       # about handler
    print(router.lookup("/home/about/me"))     # not found handler
    print(router.lookup("/home/contact"))      # not found handler

