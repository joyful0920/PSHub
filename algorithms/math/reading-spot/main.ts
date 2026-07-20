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
  const [a, b, r]: number[] = lines[0].split(" ").map(Number);
  const n: number = Number(lines[1]);
  const spots: number[][] = lines
    .slice(2, 2 + n)
    .map((line: string): number[] => line.split(" ").map(Number));

  const results: string[] = [];
  for (const [x, y] of spots) {
    // 距離 >= R を、両辺を 2 乗した「距離の 2 乗 >= R の 2 乗」で判定する。
    // sqrt を使わないので浮動小数点の誤差がなく、境界値も正しく扱える（全て整数演算）。
    const distSq: number = (x - a) ** 2 + (y - b) ** 2;
    results.push(distSq >= r ** 2 ? "silent" : "noisy");
  }

  return results.join("\n");
}
