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
  const [n, m]: number[] = lines[0].split(" ").map(Number);
  // 車間距離は N - 1 個（車 N 台の「間」の数）。
  const gaps: number[] = lines.slice(1, n).map(Number);

  let total: number = 0;
  for (const gap of gaps) {
    if (gap <= m) total += gap; // 「M 以下」なので M ちょうども含む
  }

  return total;
}
