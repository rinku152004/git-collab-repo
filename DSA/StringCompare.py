class StringComp:
    def backspaceCompare(self,s:str,t:str)->bool:
        s1=[]
        t1=[]
        
        for ch in s:
            if ch != "#":
                s1.append(ch)
            elif len(s1)>0:
                s1.pop()

        for ch in t:
            if ch != "#":
                t1.append(ch)
            elif len(t1)>0:
                t1.pop()

        if s1==t1:
            print("Both strings are equal")
            print(f"s1 is:{s1} and t1 is:{t1}")
        else:
            print("Strings are not equal")

sol = StringComp()
s=input("Enter string s:")
t=input("Enetr string t:")
sol.backspaceCompare(s,t) 