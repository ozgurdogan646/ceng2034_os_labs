#!/bin/bash

sudo mkdir /jail
sudo mkdir /jail/{bin,etc}
sudo mkdir -p /jail/{lib/x86_64-linux-gnu,lib64}
sudo cp /bin/bash /jail/bin/
sudo cp /bin/ls /jail/bin/
for i in /lib/x86_64-linux-gnu/libtinfo.so.5 /lib/x86_64-linux-gnu/libdl.so.2 /lib/x86_64-linux-gnu/libc.so.6 ; do sudo cp -v $i /jail/lib/x86_64-linux-gnu/; done
sudo cp /lib64/ld-linux-x86-64.so.2  /jail/lib64/
for i in /lib/x86_64-linux-gnu/libselinux.so.1 /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libdl.so.2 /lib/x86_64-linux-gnu/libpthread.so.0 ; do sudo cp -v $i /jail/lib/x86_64-linux-gnu/; done
sudo chroot /jail /bin/bash


