#!/usr/bin/env python3
# @_shafiqaiman_
import clipboard #pip3 install clipboard
import argparse
import sys

from func_list import *
from func_list import UNIVERSAL as mini_help
from shell_list import revshell

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('-t', '--type', metavar='', help="type of reverse shell")
parser.add_argument('-i', '--lhost', metavar='', help="listening ip address")
parser.add_argument('-p', '--lport', metavar='', help="listening port")
parser.add_argument('-l', '--list', action='store_true', help="list all the available shell")
parser.add_argument('-s', '--shell', metavar='', help="type of shell")
parser.add_argument('-o', '--output', metavar='', help="save it to the file")
parser.add_argument('-e', '--encoding', metavar='', help="encode the reverse shell")
args = parser.parse_args()
# base64, url-enc-1, url-enc-2, -e, --encoding

IDK = "[!] The payload has been copied to your clipboard\n"
IDC = "[!] The payload has been saved into your file\n"

if __name__ == '__main__':
    try:
        if args.help:
            help_me()
        elif args.list:
            list_all()
        elif args.type and args.lhost and args.lport or args.shell or args.output:
            if args.shell != None:
                rshell = revshell(args.type, args.lhost, args.lport, args.shell)
                if rshell != None:
                    try:
                        output_file(args.output, rshell); print(IDC)
                    except TypeError:
                        if args.encoding == "base64":
                            print(IDK)
                            bs64shell = encode_base64(rshell)
                            print(bs64shell)
                            clipboard.copy(bs64shell)
                        else:
                            print(IDK); print(rshell); clipboard.copy(rshell)
            else:
                rshell = revshell(args.type, args.lhost, args.lport)
                if rshell != None:
                    try:
                        output_file(args.output, rshell); print(IDC)
                    except TypeError:
                        if args.encoding == "base64":
                            print(IDK)
                            bs64shell = encode_base64(rshell)
                            print(bs64shell)
                            clipboard.copy(bs64shell)
                        else:
                            print(IDK); print(rshell); clipboard.copy(rshell)
        else:
           print(mini_help) 
    except KeyboardInterrupt:
        sys.exit()
