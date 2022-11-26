comma_index = []

x= "/* Hey  oh */ This is a  */comment /* HeyHey */  abc "

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