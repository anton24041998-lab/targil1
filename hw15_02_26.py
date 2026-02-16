#TARGIL 1
grades = [78, 92, 65, 92, 81, 74, 99, 67, 88, 99]
grades.sort(reverse=True)
print(grades)
print(grades[0],grades[1],grades[2])
grades.sort()
print(grades)
print(grades[0],grades[1],grades[2])

#TARGIL 2
votes:list = []
invalid_voters=set([])
unique_voters=set([])
count=0
while True :
    _id = int(input('please enter your id number'))
    if _id == -999:
        print(votes)
        break
    if _id not in votes:
        unique_voters.add(_id)
    else :
        invalid_voters.add(_id)
    count += 1
    votes.append(_id)
    print(votes)
for item in invalid_voters:
    if item  in unique_voters:
        unique_voters.remove(item)
print(f'{unique_voters} unique voters')
print(f'{invalid_voters}invalid voters')

print(f'{count} people voted')
