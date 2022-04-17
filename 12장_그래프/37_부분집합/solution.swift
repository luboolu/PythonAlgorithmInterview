//LEET CODE 78.Subsets

class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        func dfs(_ index: Int, _ path: [Int]) {
            if path.count == nums.count {
                return
            }

            for j in (index + 1)..<nums.count {
                var newPath = path
                newPath.append(nums[j])
                result.append(newPath)
                dfs(j, newPath)
            }
        }

        var result: [[Int]] = [[]]

        for i in 0..<nums.count {
            result.append([nums[i]])
            dfs(i, [nums[i]])
        }

        return result
    }
}