class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        inBlock = False
        newline = []

        for line in source:
            i = 0
            if not inBlock:
                newline = []

            while i < len(line):
                if not inBlock and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    inBlock = True
                    i += 2
                
                elif inBlock and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    inBlock = False
                    i += 2
                
                elif not inBlock and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
                
                elif not inBlock:
                    newline.append(line[i])
                    i += 1
                else:
                    i += 1
            if not inBlock and newline:
                result.append("".join(newline))

        return result
