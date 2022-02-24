from flask import jsonify

import artifact_example_foo as foo
import artifact_example_bar as bar

def main(request):
    return jsonify(dict(result='ok', foo=foo.foo(), foo_version=foo.__version__, bar=bar.bar2(), bar_version=bar.__version__))
