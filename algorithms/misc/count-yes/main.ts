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

  // "y"（承諾）の個数を数える。
  let count: number = 0;
  for (const c of s) {
    if (c === "y") count += 1;
  }

  return count;
}
