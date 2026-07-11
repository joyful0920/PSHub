# TypeScript 練習環境

標準入力ベースのアルゴリズム問題を TypeScript で練習するためのワークスペース。
`src/main.ts` の `solve()` だけを書き換えて解く。

## セットアップ

```bash
cd algorithms
npm install
```

Node.js 20 以上。

## コマンド

| コマンド | 説明 |
| --- | --- |
| `npm run dev` | `input.txt` を標準入力に `src/main.ts` を実行 |
| `npm run check` | 型チェック |
| `npm test` | 実行結果を `output.txt` と比較 |
| `npm run build` | `src/main.ts` を JS（`dist/main.js`）にビルド |

## テンプレート

`src/main.ts` は追跡しないので、消えたら以下を貼る。

```ts
import * as readline from "node:readline";

process.stdin.resume();
process.stdin.setEncoding("utf8");

const lines: string[] = [];

const reader = readline.createInterface({
  input: process.stdin,
});

reader.on("line", (line: string) => {
  lines.push(line);
});

reader.on("close", () => {
  const answer = solve(lines);
  console.log(answer);
});

function solve(lines: string[]): string | number {
  // ここに解答を書く
  return lines[0];
}
```

## 流れ

1. `input.txt` に入力、`output.txt` に期待出力を貼る
2. `src/main.ts` の `solve()` を書く
3. `npm run dev` → `npm test` → `npm run check`

`input.txt` `output.txt` `node_modules/` `dist/` は追跡しない。

## 解答の保管

解けたらトピック別に保存してコミットする。

```
algorithms/<topic>/<problem>/
├── README.md   問題の要約とメモ（自作）
└── main.ts     解答
```
