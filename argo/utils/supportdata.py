# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""

    This was copied from CoTeDe (cotede.castelao.net). If changed/improved
      remember to suggest the same at CoTeDe.
"""

import urllib
import hashlib
import os
import shutil
from tempfile import NamedTemporaryFile


def download_file(url, md5hash):
    """ Download data file from web

        IMPROVE it to automatically extract gz files
    """
    download_block_size = 2 ** 16

    assert type(md5hash) is str

    d = os.path.expanduser("~/.pyargorc/testdata")
    if not os.path.exists(d):
        os.makedirs(d)

    hash = hashlib.md5()

    fname = os.path.join(d, os.path.basename(url))
    if os.path.isfile(fname):
        h = hashlib.md5(open(fname, 'rb').read()).hexdigest()
        if h == md5hash:
            print("Was previously downloaded: %s" % fname)
            return
        else:
            assert False, "%s already exist but doesn't match the hash: %s" % \
                    (fname, md5hash)

    remote = urllib.urlopen(url)

    with NamedTemporaryFile(delete=False) as f:
        try:
            bytes_read = 0
            block = remote.read(download_block_size)
            while block:
                f.write(block)
                hash.update(block)
                bytes_read += len(block)
                block = remote.read(download_block_size)
        except:
            if os.path.exists(f.name):
                os.remove(f.name)
                raise

    h = hash.hexdigest()
    if h != md5hash:
        os.remove(f.name)
        print("Downloaded file doesn't match. %s" % h)
        assert False, "Downloaded file (%s) doesn't match with expected hash (%s)" % \
                (fname, md5hash)

    shutil.move(f.name, fname)
    print("Downloaded: %s" % fname)

def download_testdata(filename):

    d = os.path.expanduser("~/.pyargorc/testdata")
    if not os.path.exists(d):
        os.makedirs(d)

    test_files = {
            '20150127_prof.nc': {
                "url": "https://dl.dropboxusercontent.com/u/26063625/argo/20150127_prof.nc",
                "md5": "cedc63d54a556e4782dbacfb2d6cfb30"},
            }

    assert filename in test_files.keys(), \
            "%s is not a valid test file" % filename

    download_file(test_files[filename]["url"], test_files[filename]["md5"])
    datafile = os.path.join(os.path.expanduser("~/.pyargorc/testdata/"),
            filename)

    return datafile
