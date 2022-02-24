import os

from flask import Flask, jsonify
import artifact_example_foo as foo
import artifact_example_bar as bar

app = Flask(__name__)

@app.route("/")
def main():
    return jsonify(dict(result='ok', foo=foo.foo(), foo_version=foo.__version__, bar=bar.bar2(), bar_version=bar.__version__))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
