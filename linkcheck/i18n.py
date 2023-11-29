# Copyright (C) 2000-2014 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
Application internationalization support.
"""

# i18n support
import locale
import gettext
import sys
import codecs

default_encoding = None


def init(domain, directory):
    """Initialize this gettext i18n module and install the gettext translator class."""
    global default_encoding
    default_encoding = locale.getpreferredencoding(False)

    translator = gettext.translation(domain, localedir=directory, fallback=True)

    import builtins
    builtins.__dict__['_'] = translator.gettext
    builtins.__dict__['_n'] = translator.ngettext


def get_encoded_writer(out=sys.stdout, encoding=None, errors='replace'):
    """Get wrapped output writer with given encoding and error handling."""
    if encoding is None:
        encoding = default_encoding
    Writer = codecs.getwriter(encoding)
    return Writer(out.buffer, errors)
