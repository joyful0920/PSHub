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

function solve(lines: string[]): number {
  const n: number = Number(lines[0]);

  let count: number = 0;
  for (const line of lines.slice(1, n + 1)) {
    const [t, ...rest]: string[] = line.split(" ");
    const [p1, p2, p3, p4, p5]: number[] = rest.map(Number);

    const total: number = p1 + p2 + p3 + p4 + p5;
    const grouped: number = t === "s" ? p2 + p3 : p4 + p5;

    if (total >= 350 && grouped >= 160) count++;
  }

  return count;
}
