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

function validate(address: string): string {
  const parts: string[] = address.split(".");

  // ちょうど 4 つに区切られていること。
  if (parts.length !== 4) return "False";

  for (const part of parts) {
    // 空セグメント（連続・先頭・末尾のドット）は不正。
    if (part === "") return "False";
    // 各セグメントは 0〜255。
    const num: number = Number(part);
    if (num < 0 || num > 255) return "False";
  }

  return "True";
}

function solve(lines: string[]): string {
  const m: number = Number(lines[0]);
  const addresses: string[] = lines.slice(1, m + 1);

  return addresses.map(validate).join("\n");
}
