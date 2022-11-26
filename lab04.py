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


def removeBetweenComma(x):

    comma_index = []

    for i in range(0 , len(x)):
        
        if x[i]=="\"":
            comma_index.append(i)


    if (len(comma_index)%2!=0):
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
        x = x.replace(word , "")
    
    return x

def removeComment(x):
    
    index = len(x)
    for i in range(len(x)-2):
        # if you see a // that means disregard everything after that.
        if x[i]=='/' and x[i+1]=='/':
            index = i
            break
    x = x[:index]
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
        x=x.replace(word , "")

    return x




f = open("sample.txt", "r")
lines = f.readlines()
out=""

for line in lines:
    line = removeComment(line)
    out = out + line.rstrip() + "SEPARATOR"


out = removeBetweenComma(out)
out = removeMultiLine(out)

# print(out)


curlyList=[]

tracker = []

error = ""







    
line = out
# iterate through the line
for i in range(len(line)):
    if line[i]=='{':
        curlyList.append(i)
    if line[i] == '}':
        if curlyList is None:
            # You have an error. Your } does not match with any.
            error = error + "\nYour } at line " + (str)(i) + "does not match with any { \n"
        else :
            
            # Store the value in tracker.
            tracker.append( (curlyList.pop() , i) )
    
    

print(curlyList)
print(tracker)

# //Have a stack for { and only pop when you see a }


