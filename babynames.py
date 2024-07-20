#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    with open(filename, 'r') as file:
        text = file.read()
    
    # Extract the year
    year_match = re.search(r'<h3 align="center">Popularity in (\d{4})</h3>', text)
    year = year_match.group(1) if year_match else 'Unknown Year'
    
    # Extract names and ranks
    name_rank_pairs = re.findall(r'<tr align="right"><td>\d+</td><td>(\w+)</td><td>(\w+)</td>', text)
    
    # Create a dictionary to store name and rank
    name_rank_dict = {}
    for name1, name2 in name_rank_pairs:
        # Extracting ranks
        rank = re.search(r'<td>(\d+)</td>', text).group(1)
        name_rank_dict[name1] = rank
        name_rank_dict[name2] = rank
    
    # Sort names alphabetically and format the output
    sorted_names = sorted(name_rank_dict.keys())
    result = [year] + [f"{name} {name_rank_dict[name]}" for name in sorted_names]
    
    return result


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        name_list = extract_names(filename)
        output = '\n'.join(name_list)
        
        if summary:
            with open(filename + '.summary', 'w') as summary_file:
                summary_file.write(output)
        else:
            print(output)

if __name__ == '__main__':
  main()
