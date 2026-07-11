const { readFileSync } = require("node:fs");
const { spawnSync } = require("node:child_process");

// input.txt を標準入力として src/main.ts を実行し、
// 出力を output.txt と比較する（末尾の改行・空白差は無視）

const input = readFileSync("input.txt", "utf8");
const expected = readFileSync("output.txt", "utf8").replace(/\s*$/, "");

const result = spawnSync("npx", ["tsx", "src/main.ts"], {
  input,
  encoding: "utf8",
  shell: true, // Windows で npx(.cmd) を実行するために必要
});

if (result.status !== 0) {
  console.error("実行エラー:");
  console.error(result.stderr || result.error);
  process.exit(1);
}

const actual = result.stdout.replace(/\s*$/, "");

if (actual === expected) {
  console.log("PASS");
  process.exit(0);
} else {
  console.log("FAIL");
  console.log("--- expected ---");
  console.log(expected);
  console.log("--- actual ---");
  console.log(actual);
  process.exit(1);
}
