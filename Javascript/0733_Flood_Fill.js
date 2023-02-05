/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    let queue = []
    queue.push([sr, sc])
    let target = image[sr][sc]
    let m = image.length
    let n = image[0].length
    image[sr][sc] = color
    while(queue.length > 0) {
        let coords = queue.shift()
        console.log(coords + "  " + image[coords[0]][coords[1]])
        if(coords[0] > 0 && image[coords[0]-1][coords[1]] == target && image[coords[0]-1][coords[1]] != color ) {
            queue.push([coords[0]-1, coords[1]])
            image[coords[0]-1][coords[1]] = color
        }
        if(coords[0] < m-1 && image[coords[0]+1][coords[1]] == target && image[coords[0]+1][coords[1]] != color) {
            queue.push([coords[0]+1, coords[1]])
            image[coords[0]+1][coords[1]] = color
        }
        if(coords[1] > 0 && image[coords[0]][coords[1]-1] == target && image[coords[0]][coords[1]-1] != color) {
            queue.push([coords[0], coords[1]-1])
            image[coords[0]][coords[1]-1] = color
        }
        if(coords[1] < n-1 && image[coords[0]][coords[1]+1] == target && image[coords[0]][coords[1]+1] != color) {
            queue.push([coords[0], coords[1]+1])
            image[coords[0]][coords[1]+1] = color
        }
    }
    return image
};