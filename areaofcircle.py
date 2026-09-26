#!/usr/bin/env python3
"""Compute area of a circle.

Usage:
  - Run interactively: python areaofcircle.py
  - With CLI: python areaofcircle.py --radius 3
"""
import argparse
import math
import sys


def area_of_circle(radius: float) -> float:
	if radius < 0:
		raise ValueError("radius must be non-negative")
	return math.pi * radius * radius


def main(argv=None):
	parser = argparse.ArgumentParser(description="Compute area of a circle")
	parser.add_argument("--radius", "-r", type=float, help="radius of the circle")
	args = parser.parse_args(argv)

	if args.radius is None:
		try:
			s = input("Enter radius: ").strip()
		except (EOFError, KeyboardInterrupt):
			print()
			return 1
		if not s:
			print("No radius provided.", file=sys.stderr)
			return 2
		try:
			radius = float(s)
		except ValueError:
			print("Invalid number.", file=sys.stderr)
			return 3
	else:
		radius = args.radius

	try:
		area = area_of_circle(radius)
	except ValueError as e:
		print(e, file=sys.stderr)
		return 4

	print(f"Radius: {radius}")
	print(f"Area: {area:.6f}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
