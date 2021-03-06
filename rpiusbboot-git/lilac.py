#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'github': 'raspberrypi/usbboot'}]
build_prefix = ['extra-x86_64', 'extra-armv6h', 'extra-armv7h', 'extra-aarch64']

def pre_build():
    aur_pre_build()
    add_arch(['armv6h', 'armv7h', 'aarch64'])
    add_makedepends(['git'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
