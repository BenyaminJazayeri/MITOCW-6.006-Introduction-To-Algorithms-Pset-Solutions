import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        w = self.width
        h = self.height
        dp = [[(float('inf'),None) for _ in range(w+2)] for _ in range(h+1)]
        for j in range(1,h+1):
            for i in range(1,w+1):
                e = self.energy(i-1,j-1)
                m = min(dp[j-1][i][0],dp[j-1][i-1][0],dp[j-1][i+1][0])
                if m==float('inf'):
                    dp[j][i] = (e ,None,(i,j))
                else:
                    dp[j][i] =  (m + e,)
                    if m == dp[j-1][i][0]:
                        dp[j][i]  += ((i,j-1),(i,j))
                    if m == dp[j-1][i-1][0]:
                        dp[j][i]  += ((i-1,j-1),(i,j))
                    if m == dp[j-1][i+1][0]:
                        dp[j][i]  += ((i+1,j-1),(i,j))
                
        answer = min(dp[h][1:w+1])
        result = []
        x = answer[2]
        while x:
            result.append((x[0]-1,x[1]-1))
            x = dp[x[1]][x[0]][1]
        return list(reversed(result))
                

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
