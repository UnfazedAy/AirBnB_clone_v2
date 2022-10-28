#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive
from the contents of the web_static folder of my AirBnB Clone repo,
using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ Generates a .tgz file """
    try:
        date = datetime.now()
        current_date = date.strftime("%y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        archived_path = (f"versions/web_static_{current_date}.tgz")
        local(f"tar -cvzf {archived_path} web_static")
        return archived_path
    except Exception:
        return None
