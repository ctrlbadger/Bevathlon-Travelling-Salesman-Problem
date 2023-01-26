# Bevathlon-Travelling-Salesman-Problem

A script for the fastest Bevathlon Route using TSP using Googles OR-TOOLS 

## Why?

The sport of Bevathlon is, given a set number of pubs, one must as a team of four, have a pint at each establishment. The fastest team to go to all pubs and arrive back at the destination is the winner. 

I am a decent coder yet a very bad drinker so I designed this script to take in a list of addresses and give me and my team the most efficient route to get round all pubs using googles OR-Tools Travelling Salesman Algorithm. In the end we came third so we didn't do too bad using it.

## How to use?

After installing all the required packages in the script, you must get a google maps API key, information on how to achieve this is found [here](https://developers.google.com/maps/documentation/distance-matrix/start#get-a-key)

Once you've received an api key change the python script and modify `API_KEY` to your key. Next input your list of addresses into the `ADDRESSES` variable and then run the program! In order to prevent excess calls to the API for such a frivolous activity the program pickles the most recently received distance matrix for the next running of the script. 

## Output of the program



For 22/23's Route of [these 20 establishments](https://goo.gl/maps/9XeKRG1bS57EaYNr7) also pictured below the corresponding output of the program gives an optimal route of 6km. The script gives the index order and then a list of the pubs in order. Also included are links to the directions on google maps, these have to be split into multiple links as google only allows 10 destinations maximum.

![bevathlon-pubs](https://user-images.githubusercontent.com/9659239/214741207-7da53d43-1c81-4fac-8538-0bd40443c27b.png)

Output:
```
Get distance matrix? y/n 
:
Objective: 6.075 kilometres
Route for vehicle 0:
 0 -> 10 -> 6 -> 9 -> 2 -> 12 -> 17 -> 18 -> 16 -> 4 -> 5 -> 7 -> 19 -> 1 -> 14 -> 15 -> 13 -> 3 -> 11 -> 8 -> 0

Route Index:
[0, 10, 6, 9, 2, 12, 17, 18, 16, 4, 5, 7, 19, 1, 14, 15, 13, 3, 11, 8, 0]

Addresses:
1: 112-114 The Parade, Leamington Spa CV32 4AQ, Warwickshire, England
2: The Old Library, 11 Bath St, Leamington Spa CV31 3AF, Warwickshire, England
3: T Js Bar, 45-47 Bath St, Leamington Spa CV31 3AG, Warwickshire, England
4: Railway Inn, 12 Clemens St, Leamington Spa CV31 2DL, Warwickshire, England
5: 34 Clemens St, Leamington Spa CV31 2DN, Warwickshire, England
6: Hope Tavern, 2 Court St, Leamington Spa CV31 1NH, Warwickshire, England
7: Pig and Fiddle, 45 High St, Leamington Spa CV31 1LN, Warwickshire, England
8: The Bowling Green Inn, 18-20 New St, Leamington Spa CV31 1HP, Warwickshire, England
9: The Town House, 2 George St, Leamington Spa CV31 1ET, Warwickshire, England
10: The Drawing Board, 18 Newbold St, Leamington Spa CV32 4HN, Warwickshire, England
11: The Greyhound, 35, Kennedy Square, Leamington Spa CV32 4SY, Warwickshire, England
12: The Clarendon, 44-46 Clarendon Ave, Leamington Spa CV32 4RZ
13: The White Horse, 4-6 Clarendon Ave, Leamington Spa CV32 5PZ, Warwickshire, England
14: The White Horse, Warwickshire, 4-6 Clarendon Ave, Leamington Spa CV32 5PZ
15: The star and garter, 4-6 Warwick St, Leamington Spa CV32 5LL, Warwickshire, England
16: Woodland Tavern, 3 Regent St, Leamington Spa CV32 5HW, Warwickshire, England
17: Murphys Bar, 33 Regent St, Leamington Spa CV32 5EJ, Warwickshire, England
18: Fizzy Moon Brewhouse and Grill, 35 Regent St, Leamington Spa CV32 5EE, Warwickshire, England
19: 41-43 Warwick St, Leamington Spa CV32 5JX
20: Tesco Express, 22-24 Parade, Leamington Spa CV32 4DN
21: 112-114 The Parade, Leamington Spa CV32 4AQ, Warwickshire, England

Press Enter to see Google Map Directions:

https://www.google.com/maps/dir/112-114%2BThe%2BParade%252C%2BLeamington%2BSpa%2BCV32%2B4AQ%252C%2BWarwickshire%252C%2BEngland/The%2BOld%2BLibrary%252C%2B11%2BBath%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B3AF%252C%2BWarwickshire%252C%2BEngland/T%2BJs%2BBar%252C%2B45-47%2BBath%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B3AG%252C%2BWarwickshire%252C%2BEngland/Railway%2BInn%252C%2B12%2BClemens%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B2DL%252C%2BWarwickshire%252C%2BEngland/34%2BClemens%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B2DN%252C%2BWarwickshire%252C%2BEngland/Hope%2BTavern%252C%2B2%2BCourt%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B1NH%252C%2BWarwickshire%252C%2BEngland/Pig%2Band%2BFiddle%252C%2B45%2BHigh%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B1LN%252C%2BWarwickshire%252C%2BEngland/The%2BBowling%2BGreen%2BInn%252C%2B18-20%2BNew%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B1HP%252C%2BWarwickshire%252C%2BEngland/The%2BTown%2BHouse%252C%2B2%2BGeorge%2BSt%252C%2BLeamington%2BSpa%2BCV31%2B1ET%252C%2BWarwickshire%252C%2BEngland/The%2BDrawing%2BBoard%252C%2B18%2BNewbold%2BSt%252C%2BLeamington%2BSpa%2BCV32%2B4HN%252C%2BWarwickshire%252C%2BEngland/

https://www.google.com/maps/dir/The%2BGreyhound%252C%2B35%252C%2BKennedy%2BSquare%252C%2BLeamington%2BSpa%2BCV32%2B4SY%252C%2BWarwickshire%252C%2BEngland/The%2BClarendon%252C%2B44-46%2BClarendon%2BAve%252C%2BLeamington%2BSpa%2BCV32%2B4RZ/The%2BWhite%2BHorse%252C%2B4-6%2BClarendon%2BAve%252C%2BLeamington%2BSpa%2BCV32%2B5PZ%252C%2BWarwickshire%252C%2BEngland/The%2BWhite%2BHorse%252C%2BWarwickshire%252C%2B4-6%2BClarendon%2BAve%252C%2BLeamington%2BSpa%2BCV32%2B5PZ/The%2Bstar%2Band%2Bgarter%252C%2B4-6%2BWarwick%2BSt%252C%2BLeamington%2BSpa%2BCV32%2B5LL%252C%2BWarwickshire%252C%2BEngland/Woodland%2BTavern%252C%2B3%2BRegent%2BSt%252C%2BLeamington%2BSpa%2BCV32%2B5HW%252C%2BWarwickshire%252C%2BEngland/Murphys%2BBar%252C%2B33%2BRegent%2BSt%252C%2BLeamington%2BSpa%2BCV32%2B5EJ%252C%2BWarwickshire%252C%2BEngland/Fizzy%2BMoon%2BBrewhouse%2Band%2BGrill%252C%2B35%2BRegent%2BSt%252C%2BLeamington%2BSpa%2BCV32%2B5EE%252C%2BWarwickshire%252C%2BEngland/41-43%2BWarwick%2BSt%252C%2BLeamington%2BSpa%2BCV32%2B5JX/Tesco%2BExpress%252C%2B22-24%2BParade%252C%2BLeamington%2BSpa%2BCV32%2B4DN/

https://www.google.com/maps/dir/112-114%2BThe%2BParade%252C%2BLeamington%2BSpa%2BCV32%2B4AQ%252C%2BWarwickshire%252C%2BEngland/
```
