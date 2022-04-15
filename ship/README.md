The ship.py script is part of the ship simulation engine.
The simulation is nuts, it does not work as described in the script.

== Steps to Reproduce ==

    $ cat test|python3 ship.py

== Actual results ==

    x: 0, y: 0, direction: Direction.E
    x: 10, y: 0, direction: Direction.E
    x: 10, y: -3, direction: Direction.E
    x: 17, y: -3, direction: Direction.E
    x: 17, y: -3, direction: Direction.N
    x: 17, y: -14, direction: Direction.N

== Expected results ==

    x: 0, y: 0, direction: Direction.E
    x: 10, y: 0, direction: Direction.E
    x: 10, y: -3, direction: Direction.E
    x: 17, y: -3, direction: Direction.E
    x: 17, y: -3, direction: Direction.S
    x: 17, y: 8, direction: Direction.S

