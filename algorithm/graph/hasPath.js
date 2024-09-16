// const hasPath = (graph, src, dst) => {
//   const stack = [src];
//   while (stack.length > 0) {
//     const current = stack.pop();
//     for (let neighbor of graph[current]) {
//       if (neighbor === dst) return true;
//       stack.push(neighbor);
//     }
//   }
//   return false;
// };
const hasPath = (graph, src, dst) => {
  if (src === dst) return true;
  for (let neighbor of graph[src]) {
    if (hasPath(graph, neighbor, dst) === true) return true;
  }
  return false;
};

// const hasPath = (graph, src, dst) => {
//   const queue = [src];

//   while (queue.length > 0) {
//     const current = queue.shift();
//     if (current === dst) return true;
//     for (let neighbor of graph[current]) {
//       queue.push(neighbor);
//     }
//   }
//   return false;
// };
const explore = (graph, current, visited = new Set()) => {
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

console.log(hasPath(graph, "b", "c"));
console.log(explore(graph, "b"));

//directed graph
