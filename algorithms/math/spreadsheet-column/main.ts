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
  let n: number = Number(lines[0]);

  // A=1..Z=26 の「0 のない 26 進法」(bijective base-26)。
  // 各桁を取り出す前に 1 引いて 0-index にするのがポイント。
  let result: string = "";
  while (n > 0) {
    n -= 1;
    result = String.fromCharCode(65 + (n % 26)) + result; // 65 = 'A'
    n = Math.floor(n / 26);
  }

  return result;
}
