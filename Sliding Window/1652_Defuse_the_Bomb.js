var decrypt = function (code, k) {
  const n = code.length;
  const result = new Array(n).fill(0);
  if (k === 0) return result;

  const arr = code.concat(code);
  let start, end;

  if (k > 0) {
    start = 1;
    end = k;
  } else {
    start = n + k;
    end = n - 1;
    k = -k;
  }

  let windowSum = 0;
  for (let i = start; i <= end; i++) {
    windowSum += arr[i];
  }

  for (let i = 0; i < n; i++) {
    result[i] = windowSum;
    windowSum -= arr[start++];
    windowSum += arr[++end];
  }

  return result;
};
