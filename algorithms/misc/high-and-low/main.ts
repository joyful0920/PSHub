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
  const [a, b]: number[] = lines[0].split(" ").map(Number);
  const n: number = Number(lines[1]);
  const cards: number[][] = lines
    .slice(2, n + 2)
    .map((line: string): number[] => line.split(" ").map(Number));

  const results: string[] = [];
  for (const [first, second] of cards) {
    // 1 つ目は大きい方が強い。同点なら 2 つ目は「小さい方」が強い（向きが逆）。
    if (a > first) results.push("High");
    else if (a < first) results.push("Low");
    else if (b < second) results.push("High");
    else results.push("Low");
    // 完全同点は「同じカードは存在しない」制約により起きない。
  }

  return results.join("\n");
}
