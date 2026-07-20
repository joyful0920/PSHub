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
  const [m, n]: number[] = lines[0].split(" ").map(Number);

  const problems: string[] = [];

  // 足し算: a + b（結果が 0〜99 なので a + b <= 99）。順に M 個。
  // (a, b) を体系的に列挙するので重複は自然に生じない。
  let added: number = 0;
  for (let a: number = 0; a <= 99 && added < m; a++) {
    for (let b: number = 0; a + b <= 99 && added < m; b++) {
      problems.push(`${a} + ${b} =`);
      added += 1;
    }
  }

  // 引き算: a - b（結果が 0 以上なので a >= b）。順に N 個。
  let subbed: number = 0;
  for (let a: number = 0; a <= 99 && subbed < n; a++) {
    for (let b: number = 0; b <= a && subbed < n; b++) {
      problems.push(`${a} - ${b} =`);
      subbed += 1;
    }
  }

  return problems.join("\n");
}
