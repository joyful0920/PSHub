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
  const n: number = Number(lines[0]);
  const floors: number[] = lines.slice(1, n + 1).map(Number);

  // 最初は必ず 1 階。各ログへの移動距離を絶対値で足していく。
  let now: number = 1;
  let total: number = 0;
  for (const floor of floors) {
    total += Math.abs(floor - now);
    now = floor;
  }

  return total;
}
