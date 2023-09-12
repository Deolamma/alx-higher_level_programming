#!/usr/bin/python3
"""
Script to Load, Add and Save JSON string representation to a file
"""


if __name__ == "__main__":
    import sys
    load_from_json_file = __import__(
                                      '6-load_from_json_file'
                                    ).load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        cli_args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        cli_args = []
    cli_args.extend([arg for i, arg in enumerate(sys.argv) if i != 0])
    save_to_json_file(cli_args, "add_item.json")
