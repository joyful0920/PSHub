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
  const s1: string = lines[0];
  const s2: string = lines[1];

  let result: string = "No";
  if (s1.length !== s2.length) {
    return result;
  } else {
    for (let i: number = 0; i < s1.length; i++) {
      if (s1[i] !== s2[i]) return result;
    }

    result = "Yes";
    return result;
  }
}
