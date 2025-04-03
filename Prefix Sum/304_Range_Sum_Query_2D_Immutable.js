/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
    if (matrix.length === 0 || matrix[0].length === 0) return;

    this.rows = matrix.length;
    this.cols = matrix[0].length;

    this.sumMatrix = Array(this.rows + 1).fill(0).map(() => Array(this.cols + 1).fill(0));

    for (let i = 1; i <= this.rows; i++) {
        for (let j = 1; j <= this.cols; j++) {
            this.sumMatrix[i][j] = matrix[i-1][j-1] 
                                 + this.sumMatrix[i-1][j] 
                                 + this.sumMatrix[i][j-1] 
                                 - this.sumMatrix[i-1][j-1];
        }
    }
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    return this.sumMatrix[row2 + 1][col2 + 1] 
         - this.sumMatrix[row1][col2 + 1] 
         - this.sumMatrix[row2 + 1][col1] 
         + this.sumMatrix[row1][col1];
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */