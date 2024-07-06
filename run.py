#!/usr/bin/python
import os, sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--deploy", action="store_true")
    parser.add_argument("--build", action="store_true")
    
    args = parser.parse_args()
    
    if args.serve:
        os.system("python.exe -m mkdocs serve")
    elif args.deploy:
        os.system("python.exe -m mkdocs gh-deploy")
    elif args.build:
        os.system("python.exe -m mkdocs build")


if __name__ == "__main__":
    main()
