def average(data:list[int|float])->float:
    sum=0
    count=0
    for entry in data:
        count+=1
        sum = sum + entry
    return  sum / count 

"""
    #step 1: read the file
    #step 2: separating the 2 columns in my data.txt
    #step 3: clean the data
    #step 4: for each entry in cleaned data:
            #a) provide label "salary" for first column
            #b) provide label "name" for second column
            #c) make a new dictionary for each row

    ## BONUS: You can all dictionaries made from step 4 into 1 combined larger dictionary

    #             sep_fn                        clean_fn
    #file_data------------>seprated_file_data------------>cleaned_separated_file_data
"""

def read_data_make_dictionary(path : str) -> dict:

    with open(path) as f1:
        file_data = f1.readlines()

    sep_fn = lambda entry :  entry.split(" ")
    clean_fn = lambda mini_list :  [ mini_list[0],   mini_list[1].replace("\n"," ")   ]
    
    #separated file data: map first lambda function to original file data
    seperated_file_data = list ( map(sep_fn, file_data) )

    #the separated data will be cleaned : map second lambda function to the output of previous step
    cleaned_separated_file_data = list (    map(clean_fn,  seperated_file_data)     )

    #now use all entried in cleaned_separated_file_data to make individual dictionaries
    dict_rows = [     {"name" : entry[1],  "salary" : entry[0]}      for entry in cleaned_separated_file_data    ]

    return dict_rows



def calculate_average(path: str):
    with open(path) as f1:
        ## read all lines from this file and make a list object for each
        #a)replace \n with ""
        #b)converted replaced string into int type
        
        file_data = [         int( line.replace("\n","") )  for line in f1.readlines()]
        print(f"The average salary is : {average(file_data)}")