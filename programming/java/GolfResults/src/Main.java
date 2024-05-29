import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 選手名とスコアを入力
        System.out.println("選手1の名前を入力してください:");
        String player1Name = scanner.nextLine().trim();
        int[] player1Scores = readScores(scanner);

        System.out.println("選手2の名前を入力してください:");
        String player2Name = scanner.nextLine().trim();
        int[] player2Scores = readScores(scanner);
        
        // 選手オブジェクトを作成
        Player player1 = new Player(player1Name, player1Scores);
        Player player2 = new Player(player2Name, player2Scores);
        
        // スコアを表示
        System.out.println("選手1: " + player1.getName() + ", スコア: " + player1.getTotalScore());
        System.out.println("選手2: " + player2.getName() + ", スコア: " + player2.getTotalScore());
        
        // 勝敗を判定
        if (player1.getTotalScore() < player2.getTotalScore()) {
            System.out.println(player1.getName() + "の勝利です！");
        } else if (player1.getTotalScore() > player2.getTotalScore()) {
            System.out.println(player2.getName() + "の勝利です！");
        } else {
            System.out.println("引き分けです。");
        }
    }

    private static int[] readScores(Scanner scanner) {
        System.out.println("36個のスコアを入力してください:");
        String input = scanner.nextLine().trim();
        String[] scoreStrings = input.split(",");
        int[] scores = new int[18];
        for (int i = 0; i < 18; i++) {
            try {
                scores[i] = Integer.parseInt(scoreStrings[i + 2].trim());
                if (scores[i] <= 0) {
                    System.out.println("無効な入力です。正の整数を入力してください。");
                    return new int[0];
                }
            } catch (NumberFormatException e) {
                System.out.println("無効な入力です。数字以外が含まれています。");
                return new int[0];
            }
        }
        return scores;
    }
}
