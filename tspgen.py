#!/usr/bin/env python3

import sys

from UI import TSPGenUI

def main():
	ui = TSPGenUI()
	sys.exit(ui.exec_())

if __name__ == "__main__":
	main()
