//LEET CODE 46.Permetations

class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        func dfs(_ num: [Int], _ index: Int, _ path: [Int]) {

            if index == num.count - 1 {
                result.append(path)
                return
            }

            for n in nums {
                if path.contains(n) == false {
                    var newPath: [Int] = path

                    newPath.append(n)
                    dfs(num, index + 1, newPath)
                }
            }
        }

        //nums의 조합으로 가능한 모든 순열을 return
        var result: [[Int]] = []

        for i in 0..<nums.count {
            dfs(nums, 0, [nums[i]])
        }

        return result
    }
}