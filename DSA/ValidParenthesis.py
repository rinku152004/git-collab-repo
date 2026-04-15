# valid Parenthesis
class Parenthesis:
    def isValid(self,s:str):
        if len(s)%2==1:
            return False
        st=[]

        for ch in s:
            # opening brackets
            if ch=="(" or ch=="{" or ch=="[":
                st.append(ch)
            # closing brackets
            else:
                if len(st)==0:
                    return False
                top =st.pop()
                if ch==')' and top!='(':
                    return False
                elif ch=='}' and top!='{':
                    return False
                elif ch==']' and top!='[':
                    return False
                
        return len(st)==0
        # if len(st)==0:
        #     print("String is valid")
        #     return True
        # else: 
        #     print("String is not-valid")
        #     return False
        
para=Parenthesis()
s=input("Enter string of brackets only: ")
print(para.isValid(s))
