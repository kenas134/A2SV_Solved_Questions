from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dicts = {}
        
        for i in paths:
            arr = i.split()
            directory = arr[0]
            
            for files in arr[1:]:
                filepath, content = files.split("(")
                content = content[:-1]   # remove ')'
                
                fullpath = directory + "/" + filepath
                
                if content in dicts:
                    dicts[content].append(fullpath)
                else:
                    dicts[content] = [fullpath]
        
        # return only duplicates
        return [v for v in dicts.values() if len(v) > 1]
