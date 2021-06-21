from rich.console import Console
from rich.tree import Tree

console = Console(highlight=False)

LEVELS = [
    "medium_violet_red",
    "bright_magenta",
    "bright_cyan",
    "hot_pink3",
    "dark_goldenrod",
    "sea_green3",
]


def is_dict(obj):
    return isinstance(obj, dict)


def is_list_or_tuple(obj):
    return isinstance(obj, list) or isinstance(obj, tuple)


def is_nested(obj):
    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, float):
        return False
    elif is_dict(obj) or is_list_or_tuple(obj):
        return True
    elif "__rich_console__" in dir(obj):
        return False
    else:
        # defaulting to False for now, so that custom object just gets printed as string
        return False


def populate_tree(node, data, level=1):
    if not is_nested(data):
        node.add(data)
    elif is_dict(data):
        for k, v in data.items():
            tmp_node = node.add(f"[bold {LEVELS[level]}]{k}[/bold {LEVELS[level]}]")
            populate_tree(tmp_node, v, level + 1)
            # if not is_nested(v):
            #     node.add(f"[bold magenta]{k}[/bold magenta] [yellow]──[/yellow] {v}")
            # else:
            #     tmp_node = node.add(f"[bold magenta]{k}[/bold magenta]")
            #     populate_tree(tmp_node, v)
    elif is_list_or_tuple(data):
        for x in data:
            populate_tree(node, x)


def mate_print(data):
    if is_dict(data):
        console.print()
        data_len = len(data)
        for idx, itm in enumerate(data.items()):
            k, v = itm
            root = Tree(f"[bold {LEVELS[0]}]{k}", guide_style="yellow")
            populate_tree(root, v)
            console.print(root)
            if idx != data_len - 1 and is_nested(v):
                console.print()
        console.print()
    elif is_list_or_tuple(data):
        root = Tree("", guide_style="yellow")
        populate_tree(root, data)
        console.print(root)
        console.print()
    else:
        console.print()
        console.print(data)
        console.print()
