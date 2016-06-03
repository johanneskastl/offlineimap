# Copyright (C) 2016-2016 Nicolas Sebrecht & contributors
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

"""

The virtual imaplib2 takes care to import the correct imaplib2 library. Any
internal use of imaplib2 everywhere else in offlineimap must be done through
this virtual_imaplib2 or we might go into troubles.

"""

_SUPPORTED_RELEASE = 2
_SUPPORTED_REVISION = 53

try:
    # Try any imaplib2 in PYTHONPATH first. This allows both maintainers of
    # distributions and developers to not work with the bundled imaplib2.
    from imaplib2 import *
    import imaplib2 as imaplib

    if (int(imaplib.__release__) < _SUPPORTED_RELEASE or
            int(imaplib.__revision__) < _SUPPORTED_REVISION):
        raise ImportError("The provided imaplib2 version '%s' is not supported"%
            imaplib.__version__)
except (ImportError, NameError) as e:
    try:
        from offlineimap.bundled_imaplib2 import *
        import offlineimap.bundled_imaplib2 as imaplib
    except:
        print("Error while trying to import system imaplib2: %s"% e)
        raise

# We should really get those literals exposed by upstream. Same goes for
# __version__, __release__ and __revision__.
InternalDate = imaplib.InternalDate
Mon2num = imaplib.Mon2num
MonthNames = imaplib.MonthNames
