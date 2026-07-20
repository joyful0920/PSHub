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
  const x: string = lines[0];

  // 経過日数は 0〜364（1/1 が 0 日目）。日数の文字列に x が含まれる日を数える。
  let count: number = 0;
  for (let day: number = 0; day < 365; day++) {
    if (String(day).includes(x)) count += 1;
  }

  return count;
}
