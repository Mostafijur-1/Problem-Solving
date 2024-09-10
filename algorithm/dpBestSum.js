//Brute Force
//Time: O(n^m * m)
//Space: O(m)

//memoized
//Time: O(n * m^2)
//Space: O(m^2)

const bestSum = (targetSum, numbers, memo = {}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return [];
  if (targetSum < 0) return null;
  let shortestCombination = null;

  for (let num of numbers) {
    const remainder = targetSum - num;
    const remainderCombination = bestSum(remainder, numbers, memo);
    if (remainderCombination != null) {
      const combination = [...remainderCombination, num];

      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination;
      }
    }
  }
  memo[targetSum] = shortestCombination;
  return shortestCombination;
};

console.log(bestSum(7, [2, 3]));
console.log(bestSum(7, [5, 3, 4, 7]));
console.log(bestSum(7, [2, 4]));
console.log(bestSum(7, [2, 3, 5]));
console.log(bestSum(100, [4, 9]));
