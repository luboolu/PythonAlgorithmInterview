class Solution {

    func dfs(_ grid: inout [[Character]], _ i: Int, _ j: Int) {
        if i < 0 || i >= grid.count || j < 0 || j >= grid[i].count || grid[i][j] != "1" {
            return
        }

        grid[i][j] = "0"

        dfs(&grid, i + 1, j)
        dfs(&grid, i, j + 1)
        dfs(&grid, i - 1, j)
        dfs(&grid, i, j - 1)
    }

    func numIslands(_ grid: [[Character]]) -> Int {
        var count: Int = 0
        var grid = grid

        for i in 0..<grid.count {
            for j in 0..<grid[i].count {
                if grid[i][j] == "1" {
                    dfs(&grid, i, j)
                    count += 1
                }

            }
        }

        return count
    }
}