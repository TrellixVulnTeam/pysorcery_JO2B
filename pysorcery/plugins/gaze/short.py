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
# File: pysorcery/plugins/gaze/short.py
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
# pyGaze: short
#
#    Provide a package short description.
#
#-----------------------------------------------------------------------
"""
Provide a package short description
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
# gaze_short
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_short
#
# view the short package description
#
# Inputs
# ------
#    #param: args
#            args.spell    - List of spells to get description.
#                            Minimum 1
#            args.grimoire - 
#            args.quiet    - 
# Returns
# -------
#    @return: None
#
#-------------------------------------------------------------------------------
def gaze_short(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = lib.Package(i)
        short = spell.get_short()

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(short, 'none','white','black')
        logger.info1(message)

    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Function archive_extract
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
def parser(subparsers, parent_parser, repo_parent_parser=None):
    cmd = subparsers.add_parser('short',
                                parents = [parent_parser],
                                help = 'Display spell short description.'
    )
    cmd.add_argument('spell',
                     nargs = '+',
                     help='Display System Info'
    )
    cmd.set_defaults(func = gaze_short)
    return cmd
