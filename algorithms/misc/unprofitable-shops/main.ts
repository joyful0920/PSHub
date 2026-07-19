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
  const [n, m]: number[] = lines[0].split(" ").map(Number);
  const [a, b, c]: number[] = lines[1].split(" ").map(Number);
  const sales: number[] = lines.slice(2, 2 + n).map(Number);

  // 1 店舗あたりの費用はループ中に変わらないので外で 1 回だけ計算する。
  const cost: number = a + b * m;

  let closed: number = 0;
  for (const sold of sales) {
    // 「費用以上の利益が出ていない」= 売上利益 < 費用（ちょうど同じなら閉店しない）
    if (sold * c < cost) closed += 1;
  }

  return closed;
}
