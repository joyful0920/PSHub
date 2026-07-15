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
  const [a, b]: number[] = lines[0].split(" ").map(Number);

  const answers: number[] = [];
  for (let i: number = 0; i < 10; i++) answers.push(a + b * i);

  return answers.join(" ");
}
