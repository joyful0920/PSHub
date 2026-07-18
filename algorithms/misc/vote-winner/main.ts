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
  const votes: string[] = lines.slice(1, n + 1);

  // 名前 → 得票数 を集計。無ければ 0 から数え始める。
  const count: Record<string, number> = {};
  for (const name of votes) count[name] = (count[name] ?? 0) + 1;

  // 得票数の降順に並べ、先頭が最多得票者（同数の最多はいないと保証されている）。
  const ranked: [string, number][] = Object.entries(count).sort(
    (a: [string, number], b: [string, number]): number => b[1] - a[1],
  );

  return ranked[0][0];
}
