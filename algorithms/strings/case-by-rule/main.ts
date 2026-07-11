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
  const rule: string = lines[0];
  const text: string = lines[1];

  const result: string = [...text]
    .map((c: string): string => {
      const index: number = c.toLowerCase().charCodeAt(0) - 97;
      const isToUpperCase: boolean = "A" <= rule[index] && rule[index] <= "Z";

      return isToUpperCase ? c.toUpperCase() : c.toLowerCase();
    })
    .join("");
  return result;
}
