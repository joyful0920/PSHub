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

// ユーザー ID 末尾の通し番号を取り出す（/\d+$/ = 末尾に続く数字）。
function serial(id: string): number {
  return Number(id.match(/\d+$/)![0]);
}

function solve(lines: string[]): string {
  const n: number = Number(lines[0]);
  const ids: string[] = lines.slice(1, n + 1);

  return [...ids].sort((a, b) => serial(a) - serial(b)).join("\n");
}
