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
  const n: number = Number(lines[0]);
  const balls: number[] = lines.slice(1, n + 1).map(Number);

  const m: number = Number(lines[n + 1]);
  const passes: number[][] = lines
    .slice(n + 2, n + 2 + m)
    .map((line: string) => line.split(" ").map(Number));

  for (const [a, b, x] of passes) {
    // 宣言した数だけ渡すが、手持ちが足りなければ持っている分だけ渡す。
    const amount: number = Math.min(balls[a - 1], x);

    balls[a - 1] -= amount;
    balls[b - 1] += amount;
  }

  return balls.join("\n");
}
