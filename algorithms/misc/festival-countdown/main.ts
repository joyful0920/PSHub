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

// 1 年 = 奇数月 7 個 × 13 日 + 偶数月 6 個 × 15 日 = 181 日。
const YEAR_LENGTH: number = 181;

// その月の最終日: 偶数月は 15 日、奇数月は 13 日。
function lastDay(month: number): number {
  return month % 2 === 0 ? 15 : 13;
}

// 年初から (month, day) までの通算日数（1 月 1 日 → 1）。
function dayOfYear(month: number, day: number): number {
  let total: number = day;
  for (let mo: number = 1; mo < month; mo++) total += lastDay(mo);
  return total;
}

function solve(lines: string[]): number {
  const [y, m, d]: number[] = lines[0].split(" ").map(Number);
  const [a, b]: number[] = lines[1].split(" ").map(Number);

  // 次の開催年 = y より後で「4 で割った余りが 1」になる最小の年。
  let festivalYear: number = y + 1;
  while (festivalYear % 4 !== 1) festivalYear += 1;

  const base: number = y * YEAR_LENGTH + dayOfYear(m, d);
  const festival: number = festivalYear * YEAR_LENGTH + dayOfYear(a, b);

  return festival - base;
}
