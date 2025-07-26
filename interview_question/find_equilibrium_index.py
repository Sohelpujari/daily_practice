""" Anurag is doing a class activity, wherein every child is assigned a value.
Anurag's teacher has assigned him the responsibility of finding the leftmost child in the line,
where all the values sum to the left of that child is equal to the values sum to the right of the child."""

list = [6,1,7,3,6,5,3]

sum = sum(list)
left_sum = 0
for i in range(len(list)):
   right_sum = sum-left_sum-list[i]
   print(f"right_sum: {right_sum}")
   print(f"left_sum: {left_sum}")
   if right_sum == left_sum:
       print(i)
   left_sum += list[i]

