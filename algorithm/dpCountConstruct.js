const countConstruct = (target, wordBank, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === "") return 1;

  let totalCount = 0;

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      const numWaysRest = countConstruct(suffix, wordBank, memo);

      totalCount += numWaysRest;
    }
  }

  memo[target] = totalCount;
  return totalCount;
};

console.log(
  countConstruct("message", ["me", "e", "sag", "ss", "s", "age", "asa", "ge"])
);

console.log(
  countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "eee",
    "e",
    "ee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
