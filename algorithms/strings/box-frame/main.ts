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
  const text: string = lines[0];
  const toRepeat: number = text.length + 2;

  const answers: string[] = [];
  answers.push("+".repeat(toRepeat));
  answers.push(`+${text}+`);
  answers.push("+".repeat(toRepeat));

  return answers.join("\n");
}
