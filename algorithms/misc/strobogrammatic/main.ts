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

// 180 度回転したときの各数字の見え方。2,3,4,5,7 は回転すると数字にならない。
const ROT: Record<string, string> = {
  "0": "0",
  "1": "1",
  "8": "8",
  "6": "9",
  "9": "6",
};

// 180 度回転しても同じ数に読めるか（回転対称）。
function isSelfRotation(num: number): boolean {
  const s: string = `${num}`;

  let rotated: string = "";
  for (const ch of [...s].reverse()) {
    if (!(ch in ROT)) return false; // 回転できない数字を含む
    rotated += ROT[ch];
  }

  return rotated === s;
}

function solve(lines: string[]): number {
  const [a, b]: number[] = lines[0].split(" ").map(Number);

  let count: number = 0;
  for (let num: number = a; num <= b; num++) {
    if (isSelfRotation(num)) count += 1;
  }

  return count;
}
