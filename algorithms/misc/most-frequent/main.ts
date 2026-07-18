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
  const ids: number[] = lines[1].split(" ").map(Number);

  // ID → 出現回数 を集計。
  const count: Record<string, number> = {};
  for (const id of ids) count[id] = (count[id] ?? 0) + 1;

  // 最大出現回数を求め、その回数の ID を全て昇順で取り出す。
  const maxCount: number = Math.max(...Object.values(count));
  const winners: number[] = Object.keys(count)
    .filter((id: string): boolean => count[id] === maxCount)
    .map(Number) // キーは文字列なので数値化してから数値ソート
    .sort((a: number, b: number): number => a - b);

  return winners.join(" ");
}
