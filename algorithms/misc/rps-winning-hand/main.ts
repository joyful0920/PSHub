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

// 勝敗表: キーの手が値の手に勝つ。
const BEATS: Record<string, string> = {
  rock: "scissors",
  scissors: "paper",
  paper: "rock",
};

function solve(lines: string[]): string {
  const n: number = Number(lines[0]);
  // Set で出された手の「種類」を集める（人数ではなく種類数で勝敗が決まる）。
  const kinds: string[] = [...new Set(lines.slice(1, n + 1))];

  // 1 種類だけ・3 種類全部 → 引き分け。勝負がつくのは 2 種類のときだけ。
  if (kinds.length !== 2) return "draw";

  const [x, y]: string[] = kinds;
  return BEATS[x] === y ? x : y;
}
