class Solution:

    def generate_yhsj(self, n):
        result = []
        for i in range(1,n+1):
            row = [1 for num in range(i)]
            for j in range(1,i-1):
                row[j] = result[i-2][j-1] + result[i-2][j]  # 这里是i-2 因为 result[0]时，i=1
            result.append(row)
            print(row)
        return result

print(Solution().generate_yhsj(5))
