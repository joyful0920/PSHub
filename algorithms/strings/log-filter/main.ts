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
  solve(lines);
});

function solve(lines: string[]): void {
  const n: number = Number(lines[0]);
  const targetStr: string = lines[1];
  const words: string[] = lines.slice(2, lines.length + 1);

  let isNone: boolean = true;
  for (let i: number = 0; i < n; i++) {
    const word: string = words[i];
    if (word.includes(targetStr)) {
      isNone = false;
      console.log(word);
    }
  }

  if (isNone) console.log("None");
}
