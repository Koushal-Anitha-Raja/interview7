class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #empty array
        array=[]
        #hashset to remove the duplicates
        self.ans=set()
        #possiblities function
        self.possiblities(tiles,array)
        #return the length of array
        return len(self.ans)
    
    
    def possiblities(self,tiles,array):
        #traverse through the tiles string
        for i in range(len(tiles)):
            #append the tiles to array varaible
            array.append(tiles[i])
            #then join it with the ans hashset 
            self.ans.add("".join(array[:]))
            #recusive function with string value from starting to end
            self.possiblities(tiles[:i]+tiles[i+1:],array)
            #then backtrack it 
            array.pop()
            
        return 
