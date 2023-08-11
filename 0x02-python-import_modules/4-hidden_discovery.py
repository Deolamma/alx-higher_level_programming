#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden_data = dir(hidden_4)
    for data in hidden_data:
        if not data.startswith("_"):
            print(data)
