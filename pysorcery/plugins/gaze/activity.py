#! /usr/bin/env python3
#-----------------------------------------------------------------------
#
# Original BASH version
# Original version Copyright 2001 by Kyle Sallee
# Additions/corrections Copyright 2002 by the Source Mage Team
#
# Python rewrite
# Copyright 2017 Geoff S Derber
#
# File: pysorcery/plugins/gaze/activity.py
#
# This file is part of Sorcery.
#
#    Sorcery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License,
#    or (at your option) any later version.
#
#    Sorcery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Sorcery.  If not, see <http://www.gnu.org/licenses/>.
#
# pyGaze
#
# Gaze is part of the Sorcery source-based package management suite. It is a
# general purpose command-line tool for displaying package logs, version 
# information, checking for installed packages, checksums, message
# digests, maintainer information, package URL information, removing
# obsolete packages, displaying new packages, untracked files, sections,
# searching for files that are installed, finding when spells were
# created and packages in the software catalogue. It can even take and
# retrieve snap shots of currently installed packages for easy
# duplication.
#
#-----------------------------------------------------------------------
"""
Gaze is part of the Sorcery source-based package management suite. It is a
general purpose command-line tool for displaying package logs, version 
information, checking for installed packages, checksums, message
digests, maintainer information, package URL information, removing
obsolete packages, displaying new packages, untracked files, sections,
searching for files that are installed, finding when spells were
created and packages in the software catalogue. It can even take and
retrieve snap shots of currently installed packages for easy
duplication.
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import os
import sys

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import argparse
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes

# Other Application Libraries
from pysorcery import *
from pysorcery import lib
from pysorcery.lib import util
from pysorcery.lib.util import config
from pysorcery.lib.util import text
from pysorcery.lib.util.files import archive
# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
# Allow Color text on console
colortext = text.ConsoleText()

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
# gaze_activity
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_activity
#
# show the activity log.
# (note: this is actually a log of all that happened involving sorcery,
# such as casts, summons etc.)
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints the activity log to the console
# Return: None
#
# Status: Works on Ubuntu (subprocess)
#         Works on Source Mage
#
#-------------------------------------------------------------------------------
def gaze_activity(args):
    logger.debug('Begin Function')

    activity_files = {
        'deb'  : '/var/log/apt/history.log',
        'smgl' : '/var/log/sorcery/activity'
    }
    
    activity = lib.Files()
    activity.print_activity()

    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Function parser
#
# Extract files listed.
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
#         args.files - List of files to extract
#         args.recursive - Extract all files in all subfolders
#         args.depth (Add me) - if recursive, limit to depth #
#         args.output_dir - Directory to extract to
# Return: None
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):
    subparsers = args[0]
    parent_parsers = list(args[1:])

    activity_help = 'Show the activity log.  (Note: this is actually a log of all that happened involving sorcery, such as casts, summons etc.).'
    cmd = subparsers.add_parser('activity',
                                parents = parent_parsers,
                                help = activity_help
    )        
    cmd.set_defaults(func = gaze_activity)

    return cmd
