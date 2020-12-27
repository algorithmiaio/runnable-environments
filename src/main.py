import argparse
import yaml
import os

CRED_PATH = "~/.algorithmia/runnable.conf"


def get_auth(overwrite=None):
    if os.path.exists(CRED_PATH):
        with open(CRED_PATH) as f:
            creds = yaml.parse(f)
        if "api_key" in creds and "api_address" in creds:
            return creds
        else:
            raise Exception(f"credential file corrupt, please delete {CRED_PATH} and auth again.")
    else:
        return None


def auth(args):
    if args.overwrite:

    creds = get_auth()
    if creds:
        print("you're already authed! would you like to overwrite existing auth? Y/N")
        data = input()



def run(args):
    ...


def build(args):
    ...


def entrypoint():
    parser = argparse.ArgumentParser('algo-env', description="algo-env [<cmd>] [options]")
    subparser = parser.add_subparsers(dest='cmd')
    auth_parser = subparser.add_parser('auth', help="Record your Algorithmia API credentials")
    auth_parser.add_argument("--overwrite", action="store", type=bool, default=False,
                             help="If previously authed, will automatically overwrite without asking")

    build_parser = subparser.add_parser('build', help="Initiate a build operation")
    build_parser.add_argument("--use_cache", action="store", type=bool, default=True,
                              help="Use existing build cache, or start from scratch")
    build_parser.add_argument("--algorithm_directory", action="store", type=str, default=".",
                              help="If your algorithm is in another directory, use this to point to it")

    run_parser = subparser.add_parser('run', help="Initiate a run of your Algorithm")
    run_parser.add_argument("--algorithm_directory", action="store", type=str, default=".",
                            help="If your algorithm is in another directory, use this to point to it")

    args = parser.parse_args()

    if args.cmd == "auth":
        auth(args)
    elif args.cmd == "build":
        build(args)
    elif args.cmd == "run":
        run(args)
    else:
        raise Exception(f"command {args.cmd} is not a valid command.")
