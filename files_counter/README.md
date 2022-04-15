The application 'files_counter.py' is counting directories correctly when only
one path is specified as argument. If I specify more than one path, the results
seems to be incorrect. Please, fix the applications so that is counts files
correctly also when multiple paths are specified. Don't change the interface
of any classes and also keep the names of the internal variables and use them
as they are used!

== Steps to Reproduce ==

    $ ./files_counter.py testing_dir
    $ ./files_counter.py testing_dir/dir1 testing_dir/dir2 testing_dir/dir3

== Actual results ==

    $ ./files_counter.py testing_dir
    INFO     'testing_dir' contains 42 files
    INFO     Total number of files in selected path(s): 42

    $ ./files_counter.py testing_dir/dir1 testing_dir/dir2 testing_dir/dir3
    INFO     'testing_dir/dir1' contains 20 files
    INFO     'testing_dir/dir2' contains 32 files
    INFO     'testing_dir/dir3' contains 42 files
    INFO     Total number of files in selected path(s): 94

== Expected results ==

    $ ./files_counter.py testing_dir
    INFO     'testing_dir' contains 42 files
    INFO     Total number of files in selected path(s): 42

    $ ./files_counter.py testing_dir/dir1 testing_dir/dir2 testing_dir/dir3
    INFO     'testing_dir/dir1' contains 20 files
    INFO     'testing_dir/dir2' contains 12 files
    INFO     'testing_dir/dir3' contains 10 files
    INFO     Total number of files in selected path(s): 42

