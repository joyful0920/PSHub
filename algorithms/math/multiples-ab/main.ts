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
  const answer: string = solve(lines);
  console.log(answer);
});

function solve(lines: string[]): string {
  const [n, x, y]: number[] = lines[0].split(" ").map(Number);

  const result: string[] = [];
  for (let i: number = 1; i <= n; i++) {
    let s: string = "";
    if (i % x === 0) s += "A";
    if (i % y === 0) s += "B";
    result.push(s || "N");
  }

  return result.join("\n");
}
