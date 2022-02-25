import artifact_example_foo as foo
import artifact_example_bar as bar

__version__ = '0.0.1'

def foobar():
    return f"{foo.foo()}:{bar.bar()}"
