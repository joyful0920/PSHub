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
  const n: number = Number(lines[0]);
  const words: string[] = lines.slice(1, n + 1);

  for (let i: number = 0; i < words.length - 1; i++) {
    const a: string = words[i].slice(-1);
    const b: string = words[i + 1][0];

    if (a !== b) return `${a} ${b}`;
  }

  return "Yes";
}
