# Our solution uwu (not using much memory)
class Solution:
    def interpret(self, command: str) -> str:
        newString = ""
        for i in range(len(command)):
            if command[i] == "G":
                newString += "G"
            elif command[i] == "(" and command[i+1] == ")":
                newString += "o"
            elif command[i] == "(" and command[i+1] == "a":
                newString += "al"
        
        return newString


# One liner using string replace method (seems to be the fastest) by Keith Gally
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')

# Using dictionary
def interpret(self, s: str) -> str:
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(s)):
            tmp+=s[i]
            if(tmp in d):
                res+=d[tmp]
                tmp=""
        return res