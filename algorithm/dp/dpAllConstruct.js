const allConstruct = (target, wordBank, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === "") return [[]];

  let result = [];

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      const suffixWays = allConstruct(suffix, wordBank, memo);
      const targetWays = suffixWays.map((way) => [word, ...way]);
      result.push(...targetWays);
    }
  }

  memo[target] = result;
  return result;
};

console.log(
  allConstruct("message", ["me", "e", "sag", "ss", "s", "age", "asa", "ge"])
);

console.log(
  allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "eee",
    "e",
    "ee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
