# given the input find a way to read the {
# }

#  { and } only counts if not inside " " or nor preceded by //





# // Each line could have multiple { , } statements. 
# if a // is present anywhere to the left , everything else does not count
# use regex parsing to seaerch for two conditons. 
# { or } should not be between " " i.e ".*{.*" or ".*}.*"  . or ignore everything inside a regexp pattern. 

#ignore everything that starts with //
#   .+?(?=\/\/)
# matches eveything except the //



# "" "" ...
# " " ""
#if even remove the last one. 

# remove anything inside the ' ' and the comma. 

master_tracker = []

def removeBetweenComma(x):

    comma_index = []

    for i in range(0 , len(x)):
        
        if x[i]=="\"":
            comma_index.append(i)

    arr_length = len(comma_index)
    
    if (arr_length%2!=0):
        comma_index.pop()

    # remove everything from the comma index
    #get two at a time.

    words_to_remove=[]
    for i in range (len(comma_index)/2):
        right = comma_index.pop()
        left = comma_index.pop()
        # find the left and right and pop them. 
        words_to_remove.append(x[left:right+1])

    for word in words_to_remove:
        # In each word , track the index of the curly list.
        word_size = len(word)
        blank=""
        for i in range(word_size):
            blank=blank+" "
        x = x.replace(word , blank)

    
    return x

def removeComment(x):
    #  If // is at the beginning , replace it with a new line 
    
    index = len(x)
    
    
    if x[0]=='/' and x[1]=='/':  #If it starts with a comment
        blank = ""
        for i in range(len(x)):
            blank=blank+"~"

       
        return blank

    for i in range(len(x)-2):
        # if you see a // that means disregard everything after that.
        if x[i]=='/' and x[i+1]=='/':
            index = i
            break
    # Replace everything after // with equal amount of blank spaces.
    blank = ""
    for i in range (index , len(x)):
        blank = blank + "~"
    x = x[:index]+blank
    
    return x

def removeMultiLine(x):
    comma_index = []

   

    words_to_remove = []

    for i in range(0 , len(x)):
        
        if (x[i]=="/" and x[i+1]=='*'):
            comma_index.append(i)
        if (x[i]=='*' and x[i+1]=='/' and comma_index is not None):
            # print(comma_index.pop())
            # print(i)
            #Need to find a way if there is multiline comments.
            words_to_remove.append(x[ comma_index.pop() : i+1+1])
        



    for word in words_to_remove:
        blank=""
        # on the word check if there is a \n
        for j in range(word.count("\n")):
            blank=blank+"\n"
        for i in range(len(word)):
            blank=blank+"~"

        x=x.replace(word , blank)

    return x




f = open("sample.txt", "r")
lines = f.readlines()
out=""


#1. Prep the file for callling removebetweenComma and removeMultiline. They both require a single string.
for line in lines:
    
    line = removeComment(line)
    out = out + line.rstrip() + "SEPARATOR"

out = removeBetweenComma(out)
out = removeMultiLine(out)

# print(out)

#2.Tracking variables
#Keeps track of all {
curlyList=[]

#Keeps track of all  curly brace tuples.
tracker = []

#Keeps track of error message to be shown.
error = ""



#3. Make our new output  a single string

out = out.split("SEPARATOR")

line = ""
for l in out:
    if l == '':
        line = line + '\n'
    else:
        line = line + l +'\n'


#Have it all in one line again.
# print(line)




#4. check where all the new lines are. 



newLine_indexes=[]

for i in range(len(line)):
    if line[i]=='\n':
        newLine_indexes.append(i)



prev_index = 0
# 5. iterate through the line
for i in range(len(line)):
    
    prev_line = 0
    # if i in newLine_indexes :
    #     print( len(curlyList)  )
    #     print(line[prev_line:i])
    #     prev_line=i
    #     newLine_indexes.remove(i)
    
    
        
    
    if line[i]=='{':
        curlyList.append(i)

    if i in newLine_indexes:

        size = len(curlyList)
        size = str(size)
        
        if "}" in line[prev_index+1:i+1] :
            size = int(size)+1
            size = str(size)
            print(size + " " + line[prev_index+1 : i+1].replace('~' , " ") )
        else:
            print(  size + " " + line[prev_index+1 : i+1].replace('~' , " ") )
       
        # print(i)
        prev_index=i

    if line[i] == '}':
        if curlyList is None:
            # You have an error. Your } does not match with any.
            error = error + "\nYour } at line " + (str)(i) + "does not match with any { \n"
        else :
            
            # Store the value in tracker.
            tracker.append( (curlyList.pop() , i) )
    
    
    

# //Keep track of all the end points and then split based on that.
# if curlyList is not None:
#     print("You have a EOF error. End of line expected at line %d" , curlyList[0])
    #Find the nearest line with the help of newline Index and work from there

print(curlyList)
print(tracker)

print("The new lines are at")
print(newLine_indexes)



#How to print the final output. 

# For each line when you see


#sort the array .
tracker = tracker.sort()

