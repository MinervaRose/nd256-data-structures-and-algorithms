class Group:
    def __init__(self, _name: str) -> None:
        self.name: str = _name
        self.groups: list[Group] = []
        self.users: list[str] = []

    def add_group(self, group: 'Group') -> None:
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        self.users.append(user)

    def get_groups(self) -> list['Group']:
        return self.groups

    def get_users(self) -> list[str]:
        return self.users

    def get_name(self) -> str:
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    """
    Check if a user is in the given group or any of its sub-groups.
    """
    if user is None or group is None:
        return False

    # Use a stack to implement an iterative depth-first search
    stack = [group]

    while stack:
        current_group = stack.pop()
        # Check if the user is directly in this group
        if user in current_group.get_users():
            return True

        # Add all subgroups to the stack for further exploration
        stack.extend(current_group.get_groups())

    return False


#  Test cases
if __name__ == "__main__":
    print("\nTest Case 1: User is in a nested subgroup")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)
    print(is_user_in_group("sub_child_user", parent))  # Expected: True

    print("\nTest Case 2: User is not present in any group")
    print(is_user_in_group("ghost_user", parent))  # Expected: False

    print("\nTest Case 3: User is directly in the parent group")
    parent_user = "top_user"
    parent.add_user(parent_user)
    print(is_user_in_group("top_user", parent))  # Expected: True
