import * as readline from "node:readline";

process.stdin.resume();
process.stdin.setEncoding("utf8");

const lines: string[] = [];

const reader = readline.createInterface({
  input: process.stdin,
});

reader.on("line", (line: string) => {
  lines.push(line);
});

reader.on("close", () => {
  const answer = solve(lines);
  console.log(answer);
});

function solve(lines: string[]): string {
  const charaters: string = lines[0];

  const result = [...charaters].reverse().join("");
  return result;
}
