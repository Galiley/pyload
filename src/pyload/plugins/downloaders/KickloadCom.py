# -*- coding: utf-8 -*-

from ..base.dead_downloader import DeadDownloader


class KickloadCom(DeadDownloader):
    __name__ = "KickloadCom"
    __type__ = "downloader"
    __version__ = "0.26"
    __status__ = "stable"

    __pattern__ = r"http://(?:www\.)?kickload\.com/get/.+"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Kickload.com downloader plugin"""
    __license__ = "GPLv3"
    __authors__ = [("mkaay", "mkaay@mkaay.de")]
