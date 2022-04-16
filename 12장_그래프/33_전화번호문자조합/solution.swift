//LEET CODE 17. Letter Conbinations of a Phone Number
class Solution {
    func letterCombinations(_ digits: String) -> [String] {

        func dfs(_ index: Int, _ path: String) {
            if path.count == digits.count {
                result.append(path)
                return
            }

            for i in index..<digit.count {
                for j in numberPad[digit[i]]! {
                    let newPath = path + j
                    dfs(i + 1, newPath)
                }
            }

        }

        let numberPad: [String: [String]] = [
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]]

        let digit = digits.map({String($0)})
        var result: [String] = []


        if digits.count > 0 {
            dfs(0, "")
        }

        return result

    }
}