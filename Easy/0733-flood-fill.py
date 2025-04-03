class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image  # Prevent infinite recursion

        height, width = len(image), len(image[0])

        def dfs(sr: int, sc: int):
            # Check dimensions and see if we need to change the pixel
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == start:
                image[sr][sc] = color

                dfs(sr + 1, sc)
                dfs(sr - 1, sc)
                dfs(sr, sc + 1)
                dfs(sr, sc - 1)
        
        dfs(sr, sc)

        return image
        
