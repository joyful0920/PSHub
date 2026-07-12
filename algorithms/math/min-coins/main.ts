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
  let remaining: number = Number(lines[0]);
  const coins: number[] = [500, 100, 50, 10, 5, 1];

  let count: number = 0;
  for (const coin of coins) {
    count += Math.floor(remaining / coin);
    remaining %= coin;
  }

  return count;
}
