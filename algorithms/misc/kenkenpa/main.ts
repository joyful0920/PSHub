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
  const answer: number = solve(lines);
  console.log(answer);
});

function solve(lines: string[]): number {
  const n: number = Number(lines[0]);
  const marks: number[] = lines[1].split(" ").map(Number);

  // 連続 3 マスが (1, 1, 2) になる開始位置を数える。
  // i は n-2 未満までなら i+2 が常に範囲内（境界安全）。
  let count: number = 0;
  for (let i: number = 0; i < n - 2; i++) {
    if (marks[i] === 1 && marks[i + 1] === 1 && marks[i + 2] === 2) {
      count += 1;
    }
  }

  return count;
}
