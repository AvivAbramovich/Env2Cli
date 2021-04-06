def main(argv=None):
    from argparse import ArgumentParser
    args_parser = ArgumentParser(__package__)
    args_parser.add_argument('positional_argument')
    args_parser.add_argument('--flag', action='store_true', default=False)
    args_parser.add_argument('--other-flag', action='store_true', default=False)
    args_parser.add_argument('--some-arg')
    args_parser.add_argument('--opt-arg')
    args = args_parser.parse_args(argv)
    
    print(args)

if __name__ == '__main__':
    main()
