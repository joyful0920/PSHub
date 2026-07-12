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
  const answer: string | number = solve(lines);
  console.log(answer);
});

function solve(lines: string[]): string | number {
  const numsStr: string[] = lines[0].split(" ");
  const a: number = Number(numsStr[0]);
  const b: number = Number(numsStr[1]);

  return a > b ? a : a < b ? b : "eq";
}
