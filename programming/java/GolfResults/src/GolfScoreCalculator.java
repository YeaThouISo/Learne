public class GolfScoreCalculator {
    private final int[] parValues = {4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4};
    private int totalScore = 0;
    private int completedHoles = 0;

    public void calculateScores(String input) {
        String[] scores = input.split(",");
        for (String score : scores) {
            try {
                int shots = Integer.parseInt(score.trim());
                if (shots <= 0) {
                    System.out.println("無効な入力です。正の整数を入力してください。");
                    return;
                }
                totalScore += shots - parValues[completedHoles];
                completedHoles++;
            } catch (NumberFormatException e) {
                System.out.println("無効な入力です。数字以外が含まれています。");
                return;
            }
        }
    }

    public void displayScore() {
        System.out.println(completedHoles + " ホール終了して、" + (totalScore >= 0 ? "+" : "") + totalScore);
    }
}
