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
  const [m, n]: number[] = lines[0].split(" ").map(Number);
  const machines: number[] = lines.slice(1, m + 1).map(Number);

  // ベスト更新パターン: 1 台目で初期化し、2 台目以降と比較していく。
  let bestIndex: number = 0;
  let bestRemainder: number = n % machines[0];
  for (let i: number = 1; i < m; i++) {
    const remainder: number = n % machines[i];

    // 余りがより小さい、または同点なら容器数（machines[i]）が多い方を優先。
    if (
      remainder < bestRemainder ||
      (remainder === bestRemainder && machines[i] > machines[bestIndex])
    ) {
      bestIndex = i;
      bestRemainder = remainder;
    }
  }

  return bestIndex + 1; // 機械番号は 1 始まり
}
