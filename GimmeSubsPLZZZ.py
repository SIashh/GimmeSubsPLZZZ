#!/usr/bin/env python3

from termcolor import colored

import getopt
import sys

def check_wildcard(domain):
    '''
    Check if the domain has a wildcard configuration. It tells us if the bruteforce is applicable.
    '''
    print("TODO")

def exec_active_amass(domain):
    '''
    Execute the Amass command using active sources
    '''
    print("TODO")

def exec_assetfinder(domain):
    '''
    Execute Assetfinder, a tool that gathers subdomains using passive sources
    '''
    print("TODO")

def exec_passive_amass(domain):
    '''
    Execute the Amass command using only passive sources
    '''
    print("TODO")

def exec_subfinder(domain):
    '''
    Execute Subfinder, a tool that gathers subdomains using passive sources
    '''
    print("TODO")

def help():
    '''
    Showing the help.
    '''
    print("TODO")

if __name__ == "__main__":

    domain = ""

    if len(sys.argv) < 2:
        print("{} You should give a domain so we can find it subdomains (-d \"domain\").".format(colored("[-] ","red")))
        print("{} You can get the help using -h.".format(colored("[-] ","red")))
        exit(0)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd::", ["help", "domain="])
    except getopt.GetoptError:
        exit("{} An argument you specified is not handled. RTFM please :) (-h).".format(colored("[-]", "red")))

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            exit(0)
        elif opt in ("-d", "--domain"):
            domain = arg

    if domain != "":
        print()
    else:
        print("{} Domain missing.".format(colored("[-]", "red")))
        exit(0)
