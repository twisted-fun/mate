import sys
from rich.console import Console

console = Console()


def mprint_str(s, end="\n"):
    console.print(f"[white]{str(s)}[/white]", end=end)


def mprint_list(li):
    console.print(
        "[bold blue],[/bold blue] ".join(map(lambda x: f"[white]{str(x)}[/white]", li))
    )


def mprint_dict(d, indent=0):
    indent_inc = 0
    for idx, key in enumerate(d):
        if indent != 0 and idx != 0:
            console.print(" " * indent, "[yellow]|-[/yellow]", end=" ")
        console.print(
            f"[bold magenta]{str(key)}[/bold magenta]", "[yellow]--[/yellow]", end=" "
        )
        if isinstance(d[key], dict):
            if indent != 0:
                indent_inc = 4
            indent_inc += len(str(key))
        mprint_obj(d[key], indent + indent_inc)
        if indent == 0 and indent_inc != 0 and idx != len(list(d)) - 1:
            print()
        indent_inc = 0


def mprint_obj(o, indent=0):
    if isinstance(o, dict):
        mprint_dict(o, indent)
    elif isinstance(o, list) or isinstance(o, tuple):
        mprint_list(o)
    else:
        mprint_str(o)


def mate_print(data):
    print()
    mprint_obj(data)
    print()
