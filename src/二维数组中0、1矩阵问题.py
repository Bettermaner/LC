# 解题思路
    # 因为可以上下左右寻找最近0的距离，所以考虑双向动态规划
    # 一个动态规划只能考虑到上侧或者左侧的最近0的距离（下侧和右侧的数据还没有遍历到）
    # 考虑从左上角到右下角动态规划，再右下角到左上角动态规划。
    # 当 mat[i][j] = 0 ,dp[i][j] = 0
    # 1.dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1] + 1) , i > 0, j > 0
    # 2.dp[i][j] = min(dp[i+1][j] + 1, dp[i][j+1] + 1), i < len(mat) -1, j < len(mat[0]) -1

class Solution {
  public int[][] updateMatrix(int[][] matrix) {
    int m = matrix.length, n = matrix[0].length;
    int[][] dp = new int[m][n];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        dp[i][j] = matrix[i][j] == 0 ? 0 : 10000;
      }
    }

    // 从左上角开始
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i - 1 >= 0) {
          dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + 1);
        }
        if (j - 1 >= 0) {
          dp[i][j] = Math.min(dp[i][j], dp[i][j - 1] + 1);
        }
      }
    }
    // 从右下角开始
    for (int i = m - 1; i >= 0; i--) {
      for (int j = n - 1; j >= 0; j--) {
        if (i + 1 < m) {
          dp[i][j] = Math.min(dp[i][j], dp[i + 1][j] + 1);
        }
        if (j + 1 < n) {
          dp[i][j] = Math.min(dp[i][j], dp[i][j + 1] + 1);
        }
      }
    }
    return dp;
  }
}
