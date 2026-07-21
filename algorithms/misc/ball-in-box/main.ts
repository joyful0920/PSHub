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
  const [n, r]: number[] = lines[0].split(" ").map(Number);
  const boxes: number[][] = lines
    .slice(1, 1 + n)
    .map((line: string): number[] => line.split(" ").map(Number));

  // r は半径。箱に入るのは直径 = r * 2 以上のとき（半径と直径の取り違えに注意）。
  const diameter: number = r * 2;

  const results: number[] = [];
  for (let i: number = 0; i < n; i++) {
    const [h, w, d]: number[] = boxes[i];
    // 3 辺すべてが直径以上 = 一番短い辺が直径以上。
    if (h >= diameter && w >= diameter && d >= diameter) {
      results.push(i + 1); // 箱番号は 1 始まり
    }
  }

  return results.join("\n");
}
