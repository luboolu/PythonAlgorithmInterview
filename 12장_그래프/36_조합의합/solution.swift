//LEET CODE 39. Combination Sum

class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {

        func dfs(_ path: [Int], _ sum: Int,_ index: Int) {
            if sum == target {
                if result.contains(path.sorted()) {
                    return
                } else {
                    result.append(path.sorted())
                    return
                }
            }

            if sum >= target {
                return
            }

            for i in 0..<candidates.count {
                var newPath = path
                newPath.append(candidates[i])
                dfs(newPath, sum + candidates[i], i)
            }

        }

        var result: [[Int]] = []

        for i in 0..<candidates.count {
            dfs([candidates[i]], candidates[i], i)
        }
        return result
    }

}