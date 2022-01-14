#!/usr/bin/python3
""" Paking using Fabric """

import datetime
from fabric.api import local
import os.path


def do_pack():
    """ tgz files and give a time based name """
    the_date = datetime.now().strftime("%Y%m%d%H%M%S")
    the_pack = "versions/web_static_{}.tgz".format(the_date)
    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    local('tar -cvzf ' + the_pack + ' web_static')
    if os.path.exists(the_pack):
        return the_pack
    return None
