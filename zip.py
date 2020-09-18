students=['Ashish','Ronit','Vivek']
finals=[44,32,49]
midterms=[33,45,44]
#Dictionary Comprehension and zip
avg={pair[0]: (pair[1]+pair[2])/2  for pair in zip(students,midterms,finals)}
print("Average Score for each student is:\n{}".format(avg))