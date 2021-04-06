from env2cli import *
from main import main


Arg = Argument

argv = bulk_apply([
    Arg('POSITIONAL_ARGUMENT', func=positional_argument_func, required=True),
    Arg('FLAG_ARGUMENT', '--flag', func=flag_argument_func),
    Arg('OTHER_FLAG_ARGUMENT', '--other-flag', func=flag_argument_func),
    Arg('SOME_ARGUMENT', '--some-arg'),
    Arg('OPTIONAL_ARGUMENT', '--opt-arg')
])

print('argv: %s' % argv)

main(argv)
