- **カテゴリ**: 文字列 / ソート・ページ分割

## 問題概要

N 個の単語（小文字のみ）を辞書順に並べ、1 ページに K 個ずつ載せる。P ページ目に載る
単語（最大 K 個）を順に出力する。最終ページは K 個に満たないことがある。

## 入力フォーマット

```
N K P
s_1 s_2 ... s_N
```

## 制約

- 3 ≦ N ≦ 1000、1 ≦ K ≦ N、1 ≦ P ≦ N、単語は相異なる

## 入出力例

入力:
```
4 2 1
banana apple cherry date
```
出力:
```
apple
banana
```
（辞書順: apple banana cherry date。1 ページ目は apple, banana）

入力:
```
4 2 2
banana apple cherry date
```
出力:
```
cherry
date
```
（2 ページ目(3〜4 番目)は cherry, date）

## 解法メモ

- 単語を辞書順にソート → P ページ目は 0-index で `K*(P-1)` から K 個を `slice`。
- **文字列の既定 `sort()` は UTF-16 コード順 = 辞書順**（`"a" < "aa"`, `"abc" < "z"`）。
  数値では `sort()` が辞書順になり誤るが、文字列にはこれが正しい。
- `slice(start, start + K)` は末尾を超えても自動で丸めるので、最終ページの端数もそのまま扱える。
  計算量 O(N log N)。
