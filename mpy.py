#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import subprocess
import sys

# AMPY_PORT = "/dev/ttyUSB0"
# AMPY_BAUD = "115200"
# os.environ["AMPY_PORT"] = AMPY_PORT
# os.environ["AMPY_BAUD"] = AMPY_BAUD

load_dotenv()
args = sys.argv
args.pop(0)
args = [str(i) for i in args]
args = ["ampy"] + args
subprocess.run(args)
