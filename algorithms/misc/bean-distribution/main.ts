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
  const ages: number[] = lines.slice(1, n + 1).map(Number);

  const m: number = Number(lines[n + 1]);
  const orders: number[][] = lines
    .slice(n + 2, n + 2 + m)
    .map((line: string): number[] => line.split(" ").map(Number));

  const totals: number[] = new Array(n).fill(0);
  for (const [a, b, c] of orders) {
    // 区間 [a, b]（1 始まり）に c 個ずつ配る。ただし各自の年齢が上限。
    for (let i: number = a - 1; i <= b - 1; i++) {
      totals[i] = Math.min(totals[i] + c, ages[i]);
    }
  }

  return totals.join("\n");
}
