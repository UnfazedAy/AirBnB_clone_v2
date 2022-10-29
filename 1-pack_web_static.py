#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if os.path.isdir("versions") is False:
        os.mkdir("versions")
    d_time = datetime.now()
    current_date = d_time.strftime("%y%m%d%H%M%S")
    output = (f"versions/web_static_{current_date}.tgz")
    try:
        print(f"Packing web_static to {output}")
        local(f"tar -cvzf {output} web_static")
        size = os.stat(output).st_size
        print(f"web_static packed: {output} -> {size} Bytes")
    except Exception:
        output = None
    return output
