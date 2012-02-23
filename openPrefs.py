"""
OpenPrefs

Copyright: Erwin Santacruz, www.990adjustments.com
Written for CINEMA 4D R12.016

Name-US: OpenPrefs
Description-US: Open the Cinema 4D user preferences folder.
Make it a button for quick access.

Script tested on OS X 10.6.4 and Cinema 4D versions:
CINEMA 4D R12.016
CINEMA 4D R12.032

Creation Date: 02/21/2012
"""

import c4d
from c4d import storage


def main():
    # This is all! A simple one liner! :)
    storage.ShowInFinder(storage.GeGetC4DPath(c4d.C4D_PATH_PREFS))

if __name__=='__main__':
    main()
