#!/bin/bash

hexdump -n 4 -x just_a_file
echo tar.xz magic number
tar xf just_a_file
