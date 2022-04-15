#!/usr/bin/python3
#
# Simple application to count files under some directory.
# Copyright (C) 2016  Tomas Hozza <thozza@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import logging
import argparse


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
    handlers=(logging.StreamHandler(),)
)
LOGGER = logging.getLogger(__name__)


class FilesCounter(object):
    """
    Class representing object counting files under a certain path.
    """

    def __init__(self, path, recurse=True):
        """
        Constructor.

        :param path: path to directory in which to count files.
        :param recurse: if to look for files recursively in sub-directories
        :return: new object
        """
        self._files = list()
        self._path = None

        if not os.path.isdir(path):
            raise ValueError("%s is not a directory!", path)

        self._path = path
        self._find_files(recurse)

    def _find_files(self, recursive=True):
        """
        Find files under the given directory.

        :param recursive: If to count files recursively in the sub-directories.
        :return: list of files
        """
        for root, dirs, files in os.walk(self.path):
            if not recursive:
                dirs.clear()
            self._files.extend([os.path.join(root.lstrip(self.path), f) for f in files])

    @property
    def path(self):
        """
        Returns the path under which the object counted the files

        :return: String with path
        """
        return self._path

    @property
    def count(self):
        """
        Returns the count of files contained under the given path

        :return: Number of files
        """
        return len(self._files)


def main():
    """
    The main method.
    """
    parser = argparse.ArgumentParser(description='Simple application to count files under some directory.')
    parser.add_argument('paths',
                        metavar='PATH',
                        type=str,
                        nargs='+',
                        help='a path to directory in which to count the files.')
    parser.add_argument('--no-recursive',
                        dest='recurse',
                        action='store_false',
                        default=True,
                        help='do not inspect the directories recursively.')
    args = parser.parse_args()

    total_files = 0
    for directory in args.paths:
        try:
            counter = FilesCounter(directory, args.recurse)
        except ValueError as e:
            LOGGER.error(str(e))
            continue
        LOGGER.info("'%s' contains %d files", counter.path, counter.count)
        total_files += counter.count

    LOGGER.info("Total number of files in selected path(s): %d", total_files)


if __name__ == '__main__':
    main()
