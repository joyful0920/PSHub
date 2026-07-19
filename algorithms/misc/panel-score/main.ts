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
  const [h, w]: number[] = lines[0].split(" ").map(Number);
  // 状態グリッド（o/x の文字列 H 行）と得点グリッド（数値 H 行）を同じ添字で対応させる。
  const panels: string[] = lines.slice(1, h + 1);
  const scores: number[][] = lines
    .slice(h + 1, h + 1 + h)
    .map((line: string): number[] => line.split(" ").map(Number));

  let total: number = 0;
  for (let i: number = 0; i < h; i++) {
    for (let j: number = 0; j < w; j++) {
      if (panels[i][j] === "o") total += scores[i][j];
    }
  }

  return total;
}
