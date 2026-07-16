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
  const cards: string[] = lines[1].split(" ");

  let sum: number = 0;
  let maxCard: number = 0;
  let hasZeroCard: boolean = false;
  let hasMultiplier: boolean = false;

  for (const card of cards) {
    if (card === "0") hasZeroCard = true;
    else if (card === "x10") hasMultiplier = true;
    else {
      const n: number = Number(card);
      sum += n;

      if (n > maxCard) maxCard = n;
    }
  }

  // ルール順に適用: まず最大の点数カードを 0 点にし、その後 10 倍する。
  if (hasZeroCard) sum -= maxCard;
  if (hasMultiplier) sum *= 10;

  return sum;
}
