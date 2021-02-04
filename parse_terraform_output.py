#!/bin/python

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

component_map = {}

for line in lines:
	components = line.split()

	# Parses destruction logs
	if (len(components) >= 3 and components[1] == "Destruction" and components[2] == "complete"):
		component_map[components[0]] = "completed"
	if (len(components) >= 2 and components[1] == "Destroying..."):
		component_map[components[0]] = "Failed destroying: " + components[2]

	# Parses creation logs
	if (len(components) >= 3 and (components[1] == "Read" or components[1] == "Creation") and components[2] == "complete"):
		component_map[components[0]] = "completed"
	if (len(components) >= 2 and (components[1] == "Reading..." or components[1] == "Creating...")):
		component_map[components[0]] = "Failed " + components[1]

uncompleted_components = []

for component in component_map:
	if (component_map[component] != "completed"):
		uncompleted_components.append(component + " " + component_map[component])
		print(component_map[component] + " " + component)