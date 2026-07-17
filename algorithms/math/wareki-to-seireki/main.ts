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
  const s: string = lines[0];
  const n: number = Number(lines[1]);

  // 元年 = 開始年なので、N 年 = 開始年 + (N - 1)。
  return s === "S" ? 1926 + n - 1 : 1989 + n - 1;
}
