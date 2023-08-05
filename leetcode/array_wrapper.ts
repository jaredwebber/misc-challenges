// https://leetcode.com/problems/array-wrapper

class ArrayWrapper {
  nums: number[];
  sum: number = 0;
  constructor(nums: number[]) {
    this.nums = nums;
    nums.forEach((num) => {
      this.sum += num;
    });
  }

  valueOf() {
    return this.sum;
  }

  toString() {
    return "[" + this.nums.toString() + "]";
  }
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
