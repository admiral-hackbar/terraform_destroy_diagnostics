#!/bin/python

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

component_map = {}

for line in lines:
	components = line.split()

	if (len(components) >= 3 and components[1] == "Destruction" and components[2] == "complete"):
		component_map[components[0]] = "completed"
	if (len(components) >= 2 and components[1] == "Destroying..."):
		component_map[components[0]] = components[2]

uncompleted_components = []

for component in component_map:
	if (component_map[component] != "completed"):
		uncompleted_components.append(component + " " + component_map[component])
		print(component + " " + component_map[component])