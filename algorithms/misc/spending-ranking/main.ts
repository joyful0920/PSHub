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
  const names: string[] = lines[1].split(" ");
  const m: number = Number(lines[2]);

  // 全員を 0 で初期化。購入が 1 冊もない人（N ≦ M+1 より最大 1 名）も順位に含めるため。
  const total: Record<string, number> = {};
  for (const name of names) total[name] = 0;

  for (const line of lines.slice(3, 3 + m)) {
    const [name, priceStr]: string[] = line.split(" ");
    total[name] += Number(priceStr);
  }

  // 購入費の降順に名前を並べる（同額の社員は存在しないと保証されている）。
  return names
    .slice()
    .sort((a: string, b: string): number => total[b] - total[a])
    .join("\n");
}
