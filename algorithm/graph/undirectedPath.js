const undirectedPath = (edges, nodeA, nodeB) => {
  const graph = buildGraph(edges);

  return hasPath(graph, nodeA, nodeB);
};

const hasPath = (graph, src, dst, visited = new Set()) => {
  if (src === dst) return true;
  if (visited.has(src)) return false;
  visited.add(src);

  for (let neighbor of graph[src]) {
    if (hasPath(graph, neighbor, dst, visited)) return true;
  }
  return false;
};

const buildGraph = (edges) => {
  const graph = {};
  for (let edge of edges) {
    let [a, b] = edge;

    if (!(a in graph)) graph[a] = [];
    if (!(b in graph)) graph[b] = [];

    graph[a].push(b);
    graph[b].push(a);
  }

  return graph;
};

const edges = [
  ["a", "b"],
  ["c", "d"],
  ["b", "f"],
  ["g", "c"],
];

console.log(undirectedPath(edges, "a", "g"));
