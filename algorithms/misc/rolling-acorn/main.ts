import * as readline from "node:readline";

process.stdin.resume();
process.stdin.setEncoding("utf8");

const lines: string[] = [];
const reader: readline.Interface = readline.createInterface({
  input: process.stdin,
});

reader.on("line", (line: string) => {
  lines.push(line);
});
reader.on("close", () => {
  const answer: string = solve(lines);
  console.log(answer);
});

function solve(lines: string[]): string {
  const heights: number[] = lines[1].split(" ").map(Number);

  // 累積した高さ。下り(h<=0)で減り、上り(h>0)で増える。
  // 途中で 0 を超えたら「下ってきた分より多く上ろうとした」＝エネルギー切れで NO。
  let sum: number = 0;
  for (const h of heights) {
    sum += h;
    if (sum > 0) return "NO";
  }

  return "YES";
}
