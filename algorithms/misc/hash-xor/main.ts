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
  const [, m]: number[] = lines[0].split(" ").map(Number);
  const s: string = lines[1];

  // 長さ M のブロックに分割し、各ブロックを位置ごとに XOR していく。
  // XOR の単位元は 0 なので結果を 0 で初期化しておく。
  const result: number[] = new Array(m).fill(0);
  for (let i: number = 0; i < s.length; i += m) {
    // 最後（や唯一）のブロックが短ければ "0" で M まで埋める。
    const block: string = s.slice(i, i + m).padEnd(m, "0");
    for (let j: number = 0; j < m; j++) result[j] ^= Number(block[j]);
  }

  return result.join("");
}
