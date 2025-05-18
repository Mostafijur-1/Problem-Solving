class PriorityQueue {
  constructor() {
    this.values = [];
  }
  enqueue(val, priority) {
    this.values.push({ val, priority });
    this.sort();
  }
  dequeue() {
    return this.values.shift();
  }
  sort() {
    this.values.sort((a, b) => a.priority - b.priority);
  }
  isEmpty() {
    return this.values.length === 0;
  }
}

const dijkstra = (graph, source) => {
  const distances = {};
  const previous = {};
  //   const visited = new Set();
  const pq = new PriorityQueue();
  //Initialization the node and the distances
  for (let node in graph) {
    if (node === source) {
      distances[node] = 0;
      pq.enqueue(node, 0);
    } else {
      distances[node] = Infinity;
      pq.enqueue(node, Infinity);
    }
    previous[node] = null;
  }

  while (!pq.isEmpty()) {
    const current = pq.dequeue().val;
    // if (visited.has(current)) continue;
    // visited.add(current);

    for (let neighbor in graph[current]) {
      const distance = distances[current] + graph[current][neighbor];
      if (distance < distances[neighbor]) {
        distances[neighbor] = distance;
        previous[neighbor] = current;
        pq.enqueue(neighbor, distance);
      }
    }
  }
  return { distances, previous };
};

const graph = {
  A: { B: 4, C: 2 },
  B: { A: 4, E: 3 },
  C: { A: 2, D: 2, F: 4 },
  D: { C: 2, E: 3 },
  E: { B: 3, D: 3, F: 1 },
  F: { C: 4, E: 1 },
};

const result = dijkstra(graph, "A");
console.log(result.distances); // Shortest distance from A to all nodes
console.log(result.previous);
