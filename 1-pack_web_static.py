#!/usr/bin/python3
""" Packing using Fabric """

import datetime
from fabric.api import local


def do_pack():
    """ tgz files and give a time based name """
    the_date = datetime.now().strftime("%Y%m%d%H%M%S")
    the_pack = "versions/web_static_{}.tgz".format(the_date)
    local("mkdir -p versions")
    compressed = local("tar -cvzf {} web_static".format(the_pack))
    if compressed.failed:
        return None
    return the_pack
