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
  const [n, d]: number[] = lines[0].split(" ").map(Number);
  const numbers: number[] = lines.slice(1, n).map(Number);

  let y: number = d;
  for (let i: number = 0; i < n - 1; i++) y += d - numbers[i];

  return d * y;
}
