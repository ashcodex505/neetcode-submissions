class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        #union find data strucutrue to be able to do this 
        class UnionFind:
            def __init__(self, n):
                #rank is basically length tree for each node and soo every node si basically made to 1 
                self.par = [i for i in range(n)] 
                self.rank = [1] * n  
            
            def find(self, n): 
                while n !=  self.par[n]:

                    self.par[n] = self.par[self.par[n]]
                    n = self.par[n]
                return n 
            
            def union(self, n1, n2):

                n1 = self.find(n1)
                n2 = self.find(n2)
                if n1 == n2:
                    return False 

                if self.rank[n1] > self.rank[n2]:
                    self.par[n2] = n1 
                    self.rank[n1] += self.rank[n2]
                else:
                    self.par[n1] = n2 
                    self.rank[n2] += self.rank[n1]
                return True 



        find_ds = UnionFind(len(accounts))
        #this is where algo starts and we start using union find datastrcuture 
        #hashmap that maps email of account to index of account 
        email_Indx = {} 
        for i,account in enumerate(accounts):
            for j in account[1:]:
                if j in email_Indx:
                    find_ds.union(i, email_Indx[j])
                else: 
                    email_Indx[j] = i
        #our union find data structure already has all mappings for what accounts are basically the same 
        #so now traverse throuhg hashmap of email_indx
        emailGroup = defaultdict(list)
        #results in a hashmap where every key has teh vlaue of an empty lsit 
        for email,indx in email_Indx.items():
            i = find_ds.find(indx)
            emailGroup[i].append(email)
        
        #now we need to srot the emails 
        res = []
        for indx, emails in emailGroup.items():
            
            name = accounts[indx][0]
            res.append([name] + sorted(emailGroup[indx])) 

        return res
            


            


                



        #the union find data sturcutre has the accountsindex as each tree 0 - n starting out each one is its own parent but we union them based on the emails

        


        