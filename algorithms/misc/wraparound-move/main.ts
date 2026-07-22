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
  const [w, h, n]: number[] = lines[0].split(" ").map(Number);
  let [x, y]: number[] = lines[1].split(" ").map(Number);
  const logs: string[][] = lines
    .slice(2, 2 + n)
    .map((line: string): string[] => line.split(" "));

  for (const [dir, mStr] of logs) {
    const m: number = Number(mStr);
    if (dir === "U") y += m;
    else if (dir === "D") y -= m;
    else if (dir === "R") x += m;
    else if (dir === "L") x -= m;

    // 上下端・左右端がつながっている（トーラス）。移動量が幅より大きく何周しても、
    // また負になっても、正の剰余で必ず 0〜size-1 に收める。
    x = ((x % w) + w) % w;
    y = ((y % h) + h) % h;
  }

  return `${x} ${y}`;
}
