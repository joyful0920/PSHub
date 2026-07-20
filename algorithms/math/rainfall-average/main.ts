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
  const depths: number[] = lines[1].split(" ").map(Number);

  const sum: number = depths.reduce(
    (acc: number, cur: number): number => acc + cur,
    0,
  );

  // 平均を小数点以下切り上げ。
  return Math.ceil(sum / n);
}
