public class Player {
    private final String name; // プレイヤーの名前を保持するフィールド
    private final int[] scores; // プレイヤーの各ホールのスコアを保持するフィールド

    // コンストラクタ: プレイヤーの名前とスコアの配列を受け取り、初期化する
    public Player(String name, int[] scores) {
        this.name = name;
        this.scores = scores;
    }

    // プレイヤーの名前を取得するメソッド
    public String getName() {
        return name;
    }

    // プレイヤーの総合スコアを計算するメソッド
    public int getTotalScore() {
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        return total;
    }

    // プレイヤーの各ホールのスコアを取得するメソッド
    public int[] getScores() {
        return scores;
    }
}
