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
  const [n, m, k]: number[] = lines[0].split(" ").map(Number);
  const points: number[] = lines[1].split(" ").map(Number);
  const users: number[][] = lines
    .slice(2, 2 + m)
    .map((line: string): number[] => line.split(" ").map(Number));

  const scores: number[] = [];
  for (const counts of users) {
    // スコア = 各アイテム個数 × 単価 の総和（内積）。小数第一位を四捨五入。
    let score: number = 0;
    for (let i: number = 0; i < n; i++) score += counts[i] * points[i];

    scores.push(Math.round(score));
  }

  return scores
    .slice()
    .sort((a: number, b: number): number => b - a)
    .slice(0, k)
    .join("\n");
}
