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
  const [n, down, up]: number[] = lines[0].split(" ").map(Number);
  const prices: number[] = lines.slice(1, n + 1).map(Number);

  let shares: number = 0;
  let money: number = 0;
  for (let i: number = 0; i < n; i++) {
    const price: number = prices[i];

    // 最終日は無条件で全部売る。それ以外は up 以上なら全売り。
    if (i === n - 1 || price >= up) {
      money += price * shares;
      shares = 0;
    } else if (price <= down) {
      money -= price;
      shares += 1;
    }
  }

  return money;
}
