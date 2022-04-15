The Python script 'expand_variables.py' takes a JSON file and expands
shell-like variables in its content based on the values given as options.
However, it also expands variables which were not explicitly given as
options but were present in the environment of the parent process.
This is a potential security issue, it could be abused to expose
secrets or tokens. Please fix this vulnerability but keep the interface
of the provided functions intact.

== Steps to Reproduce ==

    $ export BAR=secret
    $ ./expand_variables.py example_file.json -e FOO=b

== Actual results ==

    $ ./expand_variables.py example_file.json -e FOO=b
    {
      "hello": "b",
      "world": "secret",
      "!": "b"
    }

== Expected results ==

    $ ./expand_variables.py example_file.json -e FOO=b
    {
      "hello": "b",
      "world": "${BAR}",
      "!": "b"
    }
