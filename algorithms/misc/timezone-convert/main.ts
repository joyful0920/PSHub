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
  const n: number = Number(lines[0]);

  // ① 都市名 → UTC からのオフセット(時) を集める（順序も保持）。
  const cities: string[] = [];
  const offset: Record<string, number> = {};
  for (const line of lines.slice(1, n + 1)) {
    const [city, s]: string[] = line.split(" ");
    cities.push(city);
    offset[city] = Number(s);
  }

  // ② 投稿都市 q の現地時刻から UTC の「時」を求める。
  const [q, t]: string[] = lines[n + 1].split(" ");
  const [hh, mm]: number[] = t.split(":").map(Number);
  const utcHour: number = hh - offset[q];

  // ③ 各都市の現地時刻 = UTC + オフセット。負や 24 以上は 0〜23 に正規化。
  const result: string[] = [];
  for (const city of cities) {
    const localHour: number = (((utcHour + offset[city]) % 24) + 24) % 24;

    const hStr: string = `${localHour}`.padStart(2, "0");
    const mStr: string = `${mm}`.padStart(2, "0");
    result.push(`${hStr}:${mStr}`);
  }

  return result.join("\n");
}
