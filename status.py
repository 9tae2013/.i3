#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

i3status = Popen(['i3status', '-c', '~/.i3/i3status.conf'], stdout=PIPE, stderr=PIPE).stdout

while True:
    line = i3status.readline()
    stack = " | ".join((item.rstrip() for item in reversed(open('/home/jamie/.deft/stack.md').readlines())))
    sys.stdout.write(stack + " | " + line)
    sys.stdout.flush()

