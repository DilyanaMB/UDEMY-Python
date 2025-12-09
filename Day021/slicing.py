piano_keys=['a','b','c','d','e','f','g']

print(piano_keys[2:5]) # taking from the position(the number after that index)

print(piano_keys[:5]) # take all from start to that position

print(piano_keys[2:]) # take all from that position to end
print(piano_keys[2:5:2]) # take in this range with last number being the step
print(piano_keys[::2]) # take all in the list with step 2
print(piano_keys[::-1]) # reverse the list

# work also for tuples (1,2,3)