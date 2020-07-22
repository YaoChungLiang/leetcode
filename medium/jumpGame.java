enum Index{
    Good, Bad, Unknown
}

public class jumpGame {
    public boolean canJump(int[] nums){
        Index[] memo = new Index[nums.length];
        for(int i = 0; i < nums.length;i++){
            memo[i] = Index.Unknown;
        }
        memo[memo.length-1] = Index.Good;
        for(int i= nums.length-2;i>=0;i--){
            int furthestJump =Math.min(i+nums[i], nums.length-1);
            for(int j = i+1;j<=furthestJump;i++){
                if(memo[j]==Index.Good){
                    memo[i] = Index.Good;
                    break;
                }
            }
        }
        return memo[0] == Index.Good;
    }
}