const subgraphNums = (graph) => {
  let count = 0;
  const visited = new Set();
  for (let node in graph) {
    if (explore(graph, node, visited) === true) {
      count++;
    }
  }
  return count;
};

const explore = (graph, current, visited) => {
  if (visited.has(current)) return false;
  visited.add(current);
  for (let neighbor of graph[current]) {
    explore(graph, neighbor, visited);
  }
  return true;
};

const graph = {
  a: ["b"],
  b: ["a", "f"],
  c: ["d", "g"],
  d: ["c"],
  f: ["b"],
  g: ["c"],
};

console.log(subgraphNums(graph));
