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
  const [xc, yc, r_1, r_2]: number[] = lines[0].split(" ").map(Number);
  const n: number = Number(lines[1]);
  const xys: string[] = lines.slice(2, n + 2);

  const answers: string[] = [];
  for (let i: number = 0; i < n; i++) {
    const [x, y]: number[] = xys[i].split(" ").map(Number);

    const calcurated: number = (x - xc) ** 2 + (y - yc) ** 2;

    if (r_1 ** 2 <= calcurated && calcurated <= r_2 ** 2) answers.push("yes");
    else answers.push("no");
  }

  return answers.join("\n");
}
