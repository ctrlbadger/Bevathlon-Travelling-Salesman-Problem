# Bevathlon-Travelling-Salesman-Problem

A script for the fastest Bevathlon Route using TSP using Googles OR-TOOLS 

## Why?

The sport of Bevathlon is given a set number of pubs one must as a team of four have a pint at each. The fastest team to go to all pubs and arrive back at the destination is the winner. 

I am a decent coder yet a very bad drinker so designed this script to take in a list of addresses and give me and my team the most efficient route to get round all pubs using googles OR-Tools Travelling Salesman Algorithm. In the end we came third so not too bad.

## How to use?

After install all the required packages for python, you must get a google maps API key, information on how to achieve this is found [here](https://developers.google.com/maps/documentation/distance-matrix/start#get-a-key)

Once you've received an api key change the python script and modify `API_KEY` to your key. Next input your list of addresses into the `ADDRESSES` variable and then run the program! In order to prevent excess calls to the API for such a frivolous activity the program pickles the most recently received distance matrix for the next running of the script. 

