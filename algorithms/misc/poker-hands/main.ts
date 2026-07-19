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

// 1 手札分の役判定。出現回数のパターンで場合分けする。
function judge(hand: string): string {
  const count: Record<string, number> = {};
  for (const card of hand) count[card] = (count[card] ?? 0) + 1;

  // 2 枚以上そろった数字のカウントだけ取り出す。
  // 4 枚の手札で起こり得る形: [4] / [3] / [2,2] / [2] / []
  const pairs: number[] = Object.values(count).filter(
    (n: number): boolean => n > 1,
  );

  if (pairs.length === 0) return "No Pair";
  if (pairs.length === 2) return "Two Pair";
  if (pairs[0] === 4) return "Four Card";
  if (pairs[0] === 3) return "Three Card";
  return "One Pair";
}

function solve(lines: string[]): string {
  const n: number = Number(lines[0]);
  const hands: string[] = lines.slice(1, n + 1);

  return hands.map(judge).join("\n");
}
