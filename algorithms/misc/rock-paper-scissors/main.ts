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
  const games: string[] = lines.slice(1, n + 1);

  let wins: number = 0;
  for (const game of games) {
    const [l, r] = game.split(" ");

    if (l > r) {
      if (l !== "P" || r !== "C") wins += 1;
    } else if (l < r) {
      if (l === "C" && r === "P") wins += 1;
    }
  }

  return wins;
}
