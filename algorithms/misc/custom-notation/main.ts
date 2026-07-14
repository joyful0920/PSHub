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
  const e: string[] = lines[0].split("");

  let sum: number = 0;
  let now: number = 0;

  for (const c of e) {
    if (c === "<") now += 10;
    else if (c === "/") now += 1;
    else {
      sum += now;
      now = 0;
    }
  }

  return sum + now;
}
