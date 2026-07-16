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
  const [, m]: number[] = lines[0].split(" ").map(Number);
  const points: number[] = lines[1]
    .split(" ")
    .map((p: string) => Math.floor(Number(p) / 100));

  const sum: number = points.reduce((acc: number, cur: number) => acc + cur, 0);

  return Math.max(m - sum, 0) * 100;
}
