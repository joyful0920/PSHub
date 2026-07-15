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
  const raws: string[] = lines.slice(1, n + 1);

  let numbers: number[] = [];
  for (const raw of raws) {
    const [a, b, c]: number[] = raw.split(" ").map(Number);

    numbers.push(a + b + (24 - c));
  }

  numbers.sort((a: number, b: number) => a - b);

  return `${numbers[0]}\n${numbers[numbers.length - 1]}`;
}
