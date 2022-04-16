//LEET CODE 77.Conbinations

class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        func dfs(_ index: Int, _ path: [Int]) {
            if path.count == k {
                if result.contains(path) == false {
                    result.append(path)
                }
                return
            }

            for i in index..<nums.count {
                if path.contains(nums[i]) == false {
                    var newPath = path
                    newPath.append(nums[i])
                    dfs(i, newPath.sorted())
                }
            }
        }

        var result: [[Int]] = []
        let nums = Array(1...n)

        for i in 0...(nums.count - k) {
            dfs(i, [nums[i]])
        }

        return result
    }
}