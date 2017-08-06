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
# This file is part of Sorcery.
#
#    Sorcery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Sorcery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Sorcery.  If not, see <http://www.gnu.org/licenses/>.
#
# Apt:
#
#    These functions work with apt packages.
#
#-----------------------------------------------------------------------
"""
Apt:


"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import apt
import sys
import subprocess
import os

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib import sorcery

# Other Optional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

#-----------------------------------------------------------------------
#
# Classes
#
# AptPackage
# AptPackageVersions
# AptPackages
# AptSection
# AptSections
# AptRepository
# AptRepositories
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class AptPackage
#
# AptPackage
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class AptPackage(sorcery.BasePackage):
    def __init__(self,name):
        logger.debug("Begin Function")
        BaseSpell.__init__(self,name)

        self.cache    = apt.cache.Cache()
#        self.cache.update()
        self.cache.open()
        
        self.pkg      = self.cache[self.name]

        versions = self.pkg.versions

        self.architecture = versions[0].architecture


        self.grimoire = 'Fix Me'            
        self.dependencies = versions[0].dependencies
        self.optional_dependencies = versions[0].suggests
        self.size = versions[0].installed_size
        
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------------------
    def install(self, args):
        logger.debug("Begin Function")

        if args.reconfigure:
            subprocess.run(['dpkg-reconfigure', self.name])

            
        if args.compile:
            subprocess.run(['apt-build', 'install', self.name])
        else:
            subprocess.run(['apt-get', 'install', self.name])
                    
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------------------
    def remove(self, args):
        logger.debug("Begin Function")

        #subprocess.run(['apt-get', 'remove', self.name])

        cache = apt.cache.Cache()
        cache.open(None)
        pkg = cache[pkg_name]
        cache.update()
        pkg.mark_delete(True, purge=True)
        resolver = apt.cache.ProblemResolver(cache)
        
        if pkg.is_installed is False:
            logger.error(pkg_name + " not installed so not removed")
        else:
            for pkg in cache.get_changes():
                if pkg.mark_delete:
                    logger.info(pkg_name + " is installed and will be removed")
                    logger.info(" %d package(s) will be removed" % cache.delete_count)
                    resolver.remove(pkg)
                    
        try:
            cache.commit()
            cache.close()
        except Exception:
            logger.error("Sorry, package removal failed.")
                    
        logger.debug("End Function")
        return

#-----------------------------------------------------------------------
#
# Class AptPackages
#
# AptPackage
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class AptPackages(sorcery.BasePackages):
    pass

#-----------------------------------------------------------------------
#
# Class AptSection
#
# AptPackage
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class AptSection(sorcery.BaseSection):
    pass

#-----------------------------------------------------------------------
#
# Class AptPackage
#
# AptPackage
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class AptSections(sorcery.BaseSections):
    pass

#-----------------------------------------------------------------------
#
# Class AptPackage
#
# AptPackage
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class AptRepository(sorcery.BaseRepository):
    pass

#-----------------------------------------------------------------------
#
# Class AptRepositories
#
# AptPackage
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class AptRepositories(sorcery.BaseRepositories):
    pass

#-----------------------------------------------------------------------
#
# Functions
#
# get_description
# get_version
# get_url
# get_short
# get_section
# read_file
# is_package
# get_license
# get_size
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function get_description
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_description(name, **kwargs):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    description  = versions[0].description

    cache.close()
    return description

#-----------------------------------------------------------------------
#
# Function get_version
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: version
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_version(name, **kwargs):
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    pkg_info = pkg.versions
    version = pkg_info[0].version

    cache.close()
    return version

#-----------------------------------------------------------------------
#
# Function get_url
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: url
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_url(name, **kwargs):
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    pkg_info = pkg.versions
    url = pkg_info[0].homepage

    cache.close()
    return url

#-----------------------------------------------------------------------
#
# Function get_short
#
# Get's a package's short description.  In apt, the package's description is
# used as there isn't a short description.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_short(name, **kwargs):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    short_description  = versions[0].summary

    cache.close()
    return short_description

#-----------------------------------------------------------------------
#
# Function get_section
#
# ...
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: section
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section(name, **kwargs):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions

    pkg_section = versions[0].section

    if 'universe' in pkg_section or 'multiverse' in pkg_section:
        section = pkg_section.split('/')[1]
    else:
        section = pkg_section            

    cache.close()
    return section

#-----------------------------------------------------------------------
#
# Function read_file
#
# Get's a package's short description.  In apt, the package's description is
# used as there isn't a short description.
#
# Inputs
# ------
#    @param: name
#    @param: **kwargs
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    @error: NotImplementedError
#
#-----------------------------------------------------------------------
def read_file(name, **kwargs):
    raise NotImplementedError
    return

#-----------------------------------------------------------------------
#
# Function is_package
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def is_package(name, **kwargs):
    try:
        cache = apt.cache.Cache()
        cache.open()
        pkg = cache[name]
        cache.close()
        pkg_exists = True
    except Exception:
        pkg_exists = False
        
    return pkg_exists

#-----------------------------------------------------------------------
#
# Function get_license
#
# Get the package license
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_license(name, **kwargs):
    cache = apt.cache.Cache()
    cache.open()

    pkg = cache[name]
    versions = pkg.versions
    license_ = 'Not Implemented'

    raise NotImplementedError
    cache.close()
    
    return license_

#-----------------------------------------------------------------------
#
# Function get_size
#
# Get the package size.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: size
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_size(name, **kwargs):
    cache = apt.cache.Cache()
    cache.open()

    pkg = cache[name]
    versions = pkg.versions
    size = versions[0].size
    
    cache.close()
    
    return size

#-------------------------------------------------------------------------------
#
# Function get_repository
#
# Get's a spell's version.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: version
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
def get_repository(name=None, directory=None):
    return name, None

#-----------------------------------------------------------------------
#
# Function get_repositories
#
# Inputs
# ------
#    @param: 
#
# Returns
# -------
#    @return: repositories
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_repositories(*args, **kwargs):
    var = subprocess.check_output(['apt-cache', 'policy'])
    repositories = []
    
    for line in var.splitlines():
        if 'l=' in str(line):
            line_list=str(line).split(',')
            
            repo_main=''
            repo_sub=''
            for item in line_list:
                if 'l=' in item:
                    repo_main = item.split('=')[1]
                if 'c=' in item:
                    repo_sub = item.split('=')[1]
                if len(repo_main) > 0 and len(repo_sub) > 0:
                    repo = repo_main + ' : ' + repo_sub
                    if repo not in repositories:
                        repositories.append(repo)

    return repositories, None

#-----------------------------------------------------------------------
#
# Function get_pkg_maintainer
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: maintainer
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_pkg_maintainer(name, **kwargs):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    maintainer = 'Not Implemented'

    cache.close()

    raise NotImplementedError
    return maintainer

#-----------------------------------------------------------------------
#
# Function get_section_maintainer
#
# Inputs
# ------
#    @param: 
#
# Returns
# -------
#    @return: maintainer
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section_maintainer(name, **kwargs):
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    maintainer = 'Not Implemented'

    cache.close()

    raise NotImplementedError
    return maintainer

#---------------------------------------------------------------
#
# Function get_queue
#
# Get a list of spells in a queue.
#
# Inputs
# ------
#    @param: which-queue
#
#
# Returns
# -------
#    @return: queue
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_queue(which_queue):
    if which_queue == 'install':
        cache = apt.cache.Cache()
        cache.open(None)
        cache.upgrade()
        queue = cache.get_changes()
    elif which_queue == 'remove':
        queue = []
        logger.error('Not Implimented')
        raise NotImplementedError
    else:
        queue = []
        logger.critical('We Fucked Up')
    return queue

#---------------------------------------------------------------
#
# Function get_installed
#
# ...
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    @return:
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_installed(status):
    var = subprocess.check_output(['apt', 'list','--installed'])
    
    packages = []
    for line in var.splitlines():
        tmpline = str(line).split("'")[1]
        name = tmpline.split('/')[0]

        if 'Listi' not in name:
            packages.append(name)
            packages.append('-')
            packages.append('-')

    return packages

#-----------------------------------------------------------------------
#
# Function 
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def print_version(self,multi=False):
    logger.debug("Begin Function")
        
    if multi:
        grimoires = libcodex.Codex()
        grimoire_list = grimoires.list_grimoires()
            
        m = len(grimoire_list)
    else:
        grimoire_list = [ self.grimoire ]
        m = 1

    print_list = [ "Repository       " ]
    print_list.append("Section          ")
    print_list.append("Package          ")
    print_list.append("Repo version     ")
    print_list.append("Installed version")
    print_list.append("----------       ")
    print_list.append("-------          ")
    print_list.append("-------          ")
    print_list.append("------------     ")
    print_list.append("-----------------")


    for i in grimoire_list:
        print_list.append(i.split('/')[-1])
        print_list.append(self.section)
        print_list.append(self.name)
        print_list.append(self.version)
        print_list.append('-')

    libmisc.column_print(print_list,cols=5,columnwise=False,gap=2)
                
    logger.debug("End Function")
    return