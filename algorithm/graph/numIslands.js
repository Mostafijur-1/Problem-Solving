var numIslands = function (grid) {
  let count = 0;
  const visited = new Set();
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (explore(grid, r, c, visited) === true) {
        count++;
      }
    }
  }
  return count;
};

const explore = (grid, r, c, visited) => {
  const rowbounds = 0 <= r && r < grid.length;
  const colbounds = 0 <= c && c < grid[0].length;
  if (!rowbounds || !colbounds) return false;

  if (grid[r][c] === "0") return false;

  const position = r + "," + c;
  if (visited.has(position)) return false;
  visited.add(position);

  explore(grid, r - 1, c, visited);
  explore(grid, r + 1, c, visited);
  explore(grid, r, c - 1, visited);
  explore(grid, r, c + 1, visited);

  return true;
};

const grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];

console.log(numIslands(grid));
