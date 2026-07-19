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

// 「自分より高い人数」→ メダルの表引き。3 人以上上にいればメダルなし。
const MEDALS: Record<number, string> = { 0: "G", 1: "S", 2: "B" };

function solve(lines: string[]): string {
  const points: number[] = lines[1].split(" ").map(Number);

  return points
    .map((p: number): string => {
      // 定義どおり「自分より高い点数の人数」を数える。同点は数えないので
      // 同点者は自動的に同じメダルになる（順位ベースの繰り下げ処理は不要）。
      const higher: number = points.filter(
        (q: number): boolean => q > p,
      ).length;

      return MEDALS[higher] ?? "N";
    })
    .join("\n");
}
