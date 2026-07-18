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
  const [, k, p]: number[] = lines[0].split(" ").map(Number);
  const words: string[] = lines[1].split(" ");

  // 文字列の既定ソートは UTF-16 コード順 = 辞書順（"a" < "aa", "abc" < "z"）。
  // 数値と違い、文字列にはこれが正しい。
  const sorted: string[] = words.slice().sort();

  // P ページ目 = 0-index で K*(P-1) から K 個。slice は末尾超過を自動で丸める。
  const start: number = k * (p - 1);

  return sorted.slice(start, start + k).join("\n");
}
