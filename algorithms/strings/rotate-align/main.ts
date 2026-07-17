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
  const [, t, s]: string[] = lines[0].split(" ");
  const n: number = t.length;

  // s を右に k 回転させた文字列は s.slice(k) + s.slice(0, k)。
  // t と一致する最小の k が答え。制約より必ず見つかる。
  for (let k: number = 0; k < n; k++) {
    if (s.slice(k) + s.slice(0, k) === t) return k;
  }

  return 0;
}
