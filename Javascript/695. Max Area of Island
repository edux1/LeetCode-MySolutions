/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    let queue = []
    let m = grid.length
    let n = grid[0].length
    let max = 0
    for(let i=0; i<m; i++) {
        for(let j=0; j<n; j++) {
            let count  = 0
            if(grid[i][j] == 1) {
                queue.push([i,j])
                grid[i][j] = 2
                while(queue.length > 0) {
                    let coords = queue.shift()
                    let x = coords[0]
                    let y = coords[1]
                    count++
                    if(x > 0 && grid[x-1][y] == 1) {
                        queue.push([x-1,y])
                        grid[x-1][y] = 2
                    }
                    if(x < m-1 && grid[x+1][y] == 1) {
                        queue.push([x+1,y])
                        grid[x+1][y] = 2
                    }
                    if(y > 0 && grid[x][y-1] == 1) {
                        queue.push([x,y-1])
                        grid[x][y-1] = 2
                    }
                    if(y < n-1 && grid[x][y+1] == 1) {
                        queue.push([x,y+1])
                        grid[x][y+1] = 2
                    }
                }
                max = Math.max(max, count)
            }
        }
    }
    return max
};