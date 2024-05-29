public class GolfScoreCalculator {
    // 各ホールのパーの値を配列で保持
    private final int[] parValues = {4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4};
    private int totalScore = 0; // 総合スコアの初期値を設定
    private int completedHoles = 0; // 完了したホールの数を追跡

    // 入力からスコアを計算するメソッド
    public void calculateScores(String input) {
        String[] scores = input.split(","); // 入力をコンマで分割
        for (String score : scores) {
            try {
                int shots = Integer.parseInt(score.trim()); // スコアを整数に変換
                if (shots <= 0) {
                    System.out.println("無効な入力です。正の整数を入力してください。");
                    return;
                }
                totalScore += shots - parValues[completedHoles]; // パーとスコアの差を総合スコアに加算
                completedHoles++; // 完了したホールの数を増やす
            } catch (NumberFormatException e) {
                System.out.println("無効な入力です。数字以外が含まれています。");
                return;
            }
        }
    }

    // 結果を表示するメソッド
    public void displayScore() {
        // 完了したホールの数と総合スコアを表示
        System.out.println(completedHoles + " ホール終了して、" + (totalScore >= 0 ? "+" : "") + totalScore);
    }
}
