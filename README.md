# Radancy OA - Custom Task
Run the mongotest.py which returns a list of all of the houses in the “Uptown” neighborhood.

The MongoDB query used in the mongotest.py is 
```
table.find(
   {"houses.neighborhood": "Uptown"}, 
   {"houses": {"$elemMatch": {"neighborhood": "Uptown"}}}
)
```

