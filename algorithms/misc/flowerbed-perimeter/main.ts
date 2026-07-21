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
  const grid: string[][] = lines
    .slice(1, 1 + h)
    .map((line: string): string[] => line.split(""));

  // 花壇かどうか。範囲外は false（＝外周にはロープが要る）。
  const isBed = (r: number, c: number): boolean =>
    r >= 0 && r < h && c >= 0 && c < w && grid[r][c] === "#";

  const dirs: number[][] = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ]; // 上下左右

  let ropes: number = 0;
  for (let i: number = 0; i < h; i++) {
    for (let j: number = 0; j < w; j++) {
      if (grid[i][j] !== "#") continue;
      // 隣が花壇でない（外 or ".")辺の数 = その区画に張るロープ本数。
      for (const [di, dj] of dirs) {
        if (!isBed(i + di, j + dj)) ropes += 1;
      }
    }
  }

  return ropes;
}
