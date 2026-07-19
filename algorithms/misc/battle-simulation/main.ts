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
  const [n, l]: number[] = lines[0].split(" ").map(Number);
  const opponents: number[] = lines.slice(1, n + 1).map(Number);

  let myLevel: number = l;
  for (const level of opponents) {
    // 勝ち: 相手の半分(切り捨て)だけ上昇 / 負け: 自分が半分に / 同レベル: 変化なし
    if (myLevel > level) myLevel += Math.floor(level / 2);
    else if (myLevel < level) myLevel = Math.floor(myLevel / 2);
  }

  return myLevel;
}
