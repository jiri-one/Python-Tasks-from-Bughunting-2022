#!/usr/bin/python3
#
# Simple URL parser.
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

import logging
import argparse

from enum import Enum
from urllib.parse import urlparse


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)-8s %(message)s',
    handlers=(logging.StreamHandler(),)
)
LOGGER = logging.getLogger(__name__)


class ProtocolHandler(Enum):
    """
    Defined known handlers for various protocols.
    """
    unknown = 0
    fuse = 1
    https = 2
    curl = 3


def handle_url(url=None):
    """
    Returns handler which can be used for given type of URL.

    :param url: URL for which to determine the handler
    :type url: str
    :return: Type of the handler
    :rtype: ProtocolHandler
    """

    url = urlparse(url)
    scheme = str(url.scheme)

    if scheme in ("ftp", "nfs"):
        return ProtocolHandler.fuse
    elif scheme in ("http", "webdav"):
        return ProtocolHandler.curl
    elif scheme in ("https"):
        return ProtocolHandler.https
    else:
        return ProtocolHandler.unknown


def main():
    """
    The main method.
    """
    parser = argparse.ArgumentParser(description='Simple application to count files under some directory.')
    parser.add_argument('url',
                        metavar='URL',
                        type=str,
                        nargs='?',
                        default='',
                        help='URL for which to determine handler.')
    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        default=False,
                        help='more verbose output.')
    args = parser.parse_args()

    if args.verbose:
        LOGGER.setLevel(logging.DEBUG)

    LOGGER.debug("Handling URL: '%s'", args.url)
    if args.url:
        handler = handle_url(args.url)
    else:
        handler = handle_url()

    LOGGER.info("For URL '%s' you should use '%s' handler.", args.url, handler.name)


if __name__ == '__main__':
    main()
