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
  const numbers: number[] = lines[0].split(" ").map(Number);

  const sum: number = numbers.reduce(
    (acc: number, cur: number) => acc + cur,
    0,
  );

  return sum % 10;
}
