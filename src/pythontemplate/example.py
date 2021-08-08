import argparse


def add_one(num: int) -> int:
    if not num:
        return 0
    return num + 1


def add_with_args(num: int) -> int:
    added = add_one(num)
    return added


def parse_command_line_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='My python template.')
    parser.add_argument('--foo', type=int, help='foo help')
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_command_line_args()
    added = add_with_args(args.foo)
    print(f'added: {added}')


if __name__ == '__main__':
    main()
