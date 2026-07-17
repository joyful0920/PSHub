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
  const [[h, w], [dy, dx]]: number[][] = lines.map((line: string) =>
    line.split(" ").map(Number),
  );

  // 描画するのは「画面全体」から「コピーで再利用できる重なり矩形」を引いた分。
  return h * w - (h - Math.abs(dy)) * (w - Math.abs(dx));
}
