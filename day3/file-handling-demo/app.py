import operations

path1 = r"/home/harshit/Desktop/python-api-flask/day3/file-handling-demo/salary.txt"
#raw string: special symbols are not interpreted
path2 = r"/home/harshit/Desktop/python-api-flask/day3/file-handling-demo/data.txt"




result = operations.calculate_average(path1) 
print(result)
ans=operations.read_data_make_dictionary(path2)
print(ans)

