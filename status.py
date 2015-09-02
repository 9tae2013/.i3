#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

i3status = Popen(['i3status', '-c', '~/.i3/i3status.conf'], stdout=PIPE, stderr=PIPE).stdout
sys.stdout.write("""{ "version": 1 }\n[\n""");

while True:
    stack = " | ".join((item.rstrip() for item in open('/home/jamie/.deft/stack.md').readlines()))
    spacer = " " * 157
    status = i3status.readline().rstrip()
    sys.stdout.write("[{\"full_text\": \"%s\", \"min_width\": \"%s\", \"align\": \"center\"}, {\"full_text\": \"%s\", \"align\": \"right\"}],\n" % (stack, spacer, status));
    sys.stdout.flush()