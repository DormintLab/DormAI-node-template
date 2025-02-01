import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    send_parser = subparsers.add_parser("sender")
    recv_parser = subparsers.add_parser("recver")
    args = parser.parse_args()
    return args


def start_sender():
    pass


def start_recver():
    pass


def main(command):
    if command == "send":
        start_sender()
    elif command == "recv":
        start_recver()
    else:
        raise NotImplementedError(f"Command {command} not implemented")


if __name__ == "__main__":
    main(**vars(parse_args()))
