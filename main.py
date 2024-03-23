# .Floor gives closet integer , which is lesser than or equal to the float value.
# Result of (A//B) is same as floor (A/B)

#STEP 1

a,b = 12,5
c = a//b
print (c)              #2.4 ==> 2

#STEP 2

a,b = -12,5
c = a//b
print (c)              #-2.4 ==> -3

#STEP 3

a,b = 12,-5
c = a//b
print (c)             #-2.4 ==> -3