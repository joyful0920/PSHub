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
  const [MMdd, hhmm]: string[] = lines[0].split(" ");
  const [MM, dd]: number[] = MMdd.split("/").map(Number);
  const [hh, mm]: number[] = hhmm.split(":").map(Number);

  // 24 以上の "時" を日に繰り上げる。月は調整しない仕様。
  const newDd: number = dd + Math.floor(hh / 24);
  const newHh: number = hh % 24;

  const MMStr: string = `${MM}`.padStart(2, "0");
  const ddStr: string = `${newDd}`.padStart(2, "0");
  const hhStr: string = `${newHh}`.padStart(2, "0");
  const mmStr: string = `${mm}`.padStart(2, "0");

  return `${MMStr}/${ddStr} ${hhStr}:${mmStr}`;
}
