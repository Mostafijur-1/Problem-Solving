const largestComponent = (graph) => {
  let largest = 0;
  const visited = new Set();
  for (let node in graph) {
    const size = exploreSize(graph, node, visited);
    if (size > largest) largest = size;
  }
  return largest;
};

const exploreSize = (graph, current, visited) => {
  if (visited.has(current)) return 0;
  visited.add(current);
  let size = 1;
  for (let neighbor of graph[current]) {
    size += exploreSize(graph, neighbor, visited);
  }
  return size;
};

const graph = {
  a: ["b"],
  b: ["a", "f"],
  c: ["d", "g"],
  d: ["c"],
  f: ["b"],
  g: ["c"],
};

console.log(largestComponent(graph));
