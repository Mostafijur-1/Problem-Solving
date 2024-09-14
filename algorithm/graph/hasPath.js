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
// const hasPath = (graph, src, dst) => {
//   if (src === dst) return true;
//   for (let neighbor of graph[src]) {
//     if (hasPath(graph, neighbor, dst) === true) return true;
//   }
//   return false;
// };

const hasPath = (graph, src, dst) => {
  const queue = [src];

  while (queue.length > 0) {
    const current = queue.shift();
    if (current === dst) return true;
    for (let neighbor of graph[current]) {
      queue.push(neighbor);
    }
  }
  return false;
};

const graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

console.log(hasPath(graph, "b", "f"));
console.log(hasPath(graph, "b", "e"));
