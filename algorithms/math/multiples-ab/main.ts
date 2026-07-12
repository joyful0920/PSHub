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
  const [n, a, b]: number[] = lines[0].split(" ").map((c: string) => Number(c));

  let answer = "";
  for (let i: number = 1; i < n + 1; i++) {
    if (i % a !== 0 && i % b !== 0) answer += "N";
    else {
      if (i % a === 0) answer += "A";
      if (i % b === 0) answer += "B";
    }

    if (i !== n) answer += "\n";
  }

  return answer;
}
