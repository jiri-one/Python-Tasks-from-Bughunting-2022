The application 'url_parser.py' is parsing URLs and prints handers to use.
For URL starting with 'http://' we expect handler 'curl' but instead get
'https'. Please fix the script. Don't change the interface of any class or
function and also keep the names of the internal variables and use them as
they are used! Do also some sanity test to see whether the tool is not
having serious issues in other basic scenarios. It seems like when not
giving any argument, it behaves weird.

== Steps to Reproduce ==

    $ ./url_parser.py http://example.com
    $ ./url_parser.py

== Actual results ==

    $ ./url_parser.py http://example.com
    INFO     For URL 'http://example.com' you should use 'https' handler.

    $ ./url_parser.py
    Traceback (most recent call last):
      File "/home/bughunting/sources/url_parser/./url_parser.py", line 102, in <module>
        main()
      File "/home/bughunting/sources/url_parser/./url_parser.py", line 96, in main
        handler = handle_url()
      File "/home/bughunting/sources/url_parser/./url_parser.py", line 67, in handle_url
        elif scheme in '':
    TypeError: 'in <string>' requires string as left operand, not bytes

== Expected results ==

    $ ./url_parser.py http://example.com
    INFO     For URL 'http://example.com' you should use 'curl' handler.
    $ ./url_parser.py
    INFO     For URL '' you should use 'unknown' handler.

