/**
 * Plus One (LeetCode 66)
 *
 * Given a large integer represented as an integer array digits, where each
 * digits[i] is the ith digit of the integer. The digits are ordered from most
 * significant to least significant in left-to-right order. The large integer
 * does not contain any leading 0's.
 *
 * Increment the large integer by one and return the resulting array of digits.
 */

function plusOne(digits: number[]): number[] {
  const result = [...digits];
  let i = result.length - 1;
  let carry = 1;

  while (i >= 0 && carry > 0) {
    const sum = result[i] + carry;
    result[i] = sum % 10;
    carry = sum >= 10 ? 1 : 0;
    i--;
  }

  if (carry > 0) {
    result.unshift(1);
  }

  return result;
}

// Examples (run when file is executed)
function runExamples(): void {
  console.assert(
    JSON.stringify(plusOne([1, 2, 3])) === "[1,2,4]",
    "123 + 1 = 124"
  );
  console.assert(
    JSON.stringify(plusOne([4, 3, 2, 1])) === "[4,3,2,2]",
    "4321 + 1 = 4322"
  );
  console.assert(
    JSON.stringify(plusOne([9])) === "[1,0]",
    "9 + 1 = 10"
  );
  console.assert(
    JSON.stringify(plusOne([9, 9, 9])) === "[1,0,0,0]",
    "999 + 1 = 1000"
  );
  console.log("All examples passed.");
}

runExamples();

export { plusOne };
