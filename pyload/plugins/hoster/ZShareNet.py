# -*- coding: utf-8 -*-

from pyload.plugins.internal.DeadHoster import DeadHoster


class ZShareNet(DeadHoster):
    __name__ = "ZShareNet"
    __type__ = "hoster"
    __version__ = "0.26"
    __status__ = "stable"

    __pattern__ = r'https?://(?:ww[2w]\.)?zshares?\.net/.+'
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """ZShare.net hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("espes", None),
                   ("Cptn Sandwich", None)]