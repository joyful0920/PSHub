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

  for (let x: number = 1; x <= 9; x++) {
    for (let y: number = 0; y <= 9; y++) {
      if ((10 * x + y) * y === 100 * a + 10 * x + b) {
        return `${x} ${y}`;
      }
    }
  }

  return "No";
}
