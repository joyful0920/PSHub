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

// (月, 日) を M*100 + D の 1 つの数に符号化すると、大小比較がそのまま日付順になる。
function key([m, d]: number[]): number {
  return m * 100 + d;
}

function solve(lines: string[]): string {
  const n: number = Number(lines[0]);
  const birthdays: number[][] = lines
    .slice(1, n + 2)
    .map((line: string): number[] => line.split(" ").map(Number));

  const me: number = key(birthdays[0]);

  // 1 月 1 日起点: 自分より前（小さい）の人数 + 1。自分自身は同値なので数えない。
  const rankFromJan: number =
    1 + birthdays.filter((b: number[]): boolean => key(b) < me).length;

  // 4 月 2 日起点: 4/2 未満(< 402)の日付は 1 年後ろへ回す（+1300 で末尾に送る）。
  const shift = (v: number): number => (v >= 402 ? v : v + 1300);
  const meShifted: number = shift(me);
  const rankFromApr: number =
    1 + birthdays.filter((b: number[]): boolean => shift(key(b)) < meShifted).length;

  return `${rankFromJan}\n${rankFromApr}`;
}
