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
  const m: number = (n * (n - 1)) / 2;
  const results: number[][] = lines
    .slice(1, m + 1)
    .map((line: string): number[] => line.split(" ").map(Number));

  // N×N を "-" で初期化。行ごとに新しい配列を作るため fill 直接ではなくコールバックで生成。
  const table: string[][] = Array.from({ length: n }, () =>
    new Array(n).fill("-"),
  );

  // 1 試合につき 2 マス（勝者視点 W / 敗者視点 L）を対称に埋める。
  for (const [winner, loser] of results) {
    table[winner - 1][loser - 1] = "W";
    table[loser - 1][winner - 1] = "L";
  }

  return table.map((row: string[]): string => row.join(" ")).join("\n");
}
