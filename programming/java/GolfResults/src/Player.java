public class Player {
    private final String name;
    private final int[] scores;

    public Player(String name, int[] scores) {
        this.name = name;
        this.scores = scores;
    }

    public String getName() {
        return name;
    }

    public int getTotalScore() {
        int total = 0;
        for (int score : scores) {
            total += score;
        }
        return total;
    }

    public int[] getScores() {
        return scores;
    }
}
