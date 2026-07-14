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
  const numbers: number[] = lines.slice(1, n + 1).map(Number);

  const answer: string[] = [];
  for (const num of numbers) {
    let sum: number = 0;
    for (let i: number = 1; i < num; i++) {
      if (num % i === 0) sum += i;
    }

    if (sum === num) answer.push("perfect");
    else if (Math.abs(num - sum) === 1) answer.push("nearly");
    else answer.push("neither");
  }

  return answer.join("\n");
}
