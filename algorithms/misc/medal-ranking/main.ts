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
  const medals: number[][] = lines
    .slice(1, n + 1)
    .map((line: string): number[] => line.split(" ").map(Number));

  // 金 → 銀 → 銅 の順に降順。前のキーが同点(差 0)なら次のキーへ。
  const ranked: number[][] = medals
    .slice()
    .sort(
      (a: number[], b: number[]): number =>
        b[0] - a[0] || b[1] - a[1] || b[2] - a[2],
    );

  return ranked.map((row: number[]): string => row.join(" ")).join("\n");
}
