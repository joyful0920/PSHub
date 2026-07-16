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
  const [n, m]: number[] = lines[0].split(" ").map(Number);

  // 合格点が 0 なら全員合格。点数を読む必要もない。
  if (m === 0) {
    const all: number[] = [];
    for (let i: number = 1; i <= n; i++) all.push(i);
    return all.join("\n");
  }

  // ここでは m > 0 が確定しているので、成績がマイナスなら必ず不合格。
  // よって Math.max による 0 クランプは不要で、a - 5b >= m だけで判定できる。
  const passed: number[] = [];
  for (let i: number = 0; i < n; i++) {
    const [a, b]: number[] = lines[i + 1].split(" ").map(Number);

    if (a - 5 * b >= m) passed.push(i + 1);
  }

  return passed.join("\n");
}
