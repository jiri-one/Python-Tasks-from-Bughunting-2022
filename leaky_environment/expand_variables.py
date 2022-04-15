#!/usr/bin/python3
#
# A simple script expanding shell-like variables in a JSON.

import argparse
import contextlib
import json
import os
from typing import Dict, Any, List


@contextlib.contextmanager
def modify_environ(new_variables: Dict[str, str]):
    """A context manager for temporarily modifying os.environ and then reverting it."""
    environ_backup = os.environ.copy()
    os.environ.clear()
    os.environ.update(new_variables)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(environ_backup)


def expand_node(node: Any) -> Any:
    """Expands shell-like variables in a single node of a JSON tree structure.

    Args:
        node: The JSON node to expand.

    Returns:
        The expanded node.
    """
    if isinstance(node, str):
        return os.path.expandvars(node)
    elif isinstance(node, list):
        for i in range(len(node)):
            node[i] = expand_node(node[i])
    elif isinstance(node, dict):
        for k, v in node.items():
            node[k] = expand_node(v)
    return node


def expand_content(content: Dict[Any, Any], variables: Dict[str, str]) -> Dict[Any, Any]:
    """Expands shell-like variables in JSON values.

    Args:
        content: JSON loaded as dict to be expanded.
        variables: Key-value pairs of environment variables to expand
            in the JSON.

    Returns:
        The expanded JSON.
    """
    with modify_environ(variables):
        return expand_node(content)


def split_variables(variables: List[str]) -> Dict[str, str]:
    """Splits variables from VAR=VALUE format into key-value pairs.

    Args:
        variables: List of environment variables in VAR=VALUE format.

    Returns:
        Dict mapping variables to their values.
    """
    result = {}
    for var in variables:
        split = var.split("=")
        if len(split) != 2:
            continue
        result[split[0]] = split[1]
    return result


def parse_options() -> argparse.Namespace:
    """Parses command line arguments.

    Returns:
        Argparse namespace containing the parsed options.
    """
    parser = argparse.ArgumentParser(description="Expand shell-like variables from a JSON.")
    parser.add_argument('file', metavar='FILE', type=str,
                        help="JSON file to expand shell-like variables in.")
    parser.add_argument('-e', '--environment', action='append', default=[],
                        help='Environment variables in a VAR=VALUE format to use for expansion. '
                             'Can be specified multiple times.')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_options()
    with open(args.file, "r") as json_file:
        data = json.load(json_file)
    expanded = expand_content(data, split_variables(args.environment))
    print(json.dumps(expanded, indent=2))
