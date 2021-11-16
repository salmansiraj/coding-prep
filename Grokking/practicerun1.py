# sqrt N * log * log N from crossing out that many numbers every time we see a prime val
def countPrimes(self, n: int) -> int:
    if n <= 2:
        return 0

    numbers = {}
    for p in range(2, int(sqrt(n)) + 1):
        if p not in numbers:
            for multiple in range(p*p, n, p):
                numbers[multiple] = 1

    # substracting 1 and number n itself from n
    return n - len(numbers) - 2


def twoSumLessThanK(arr, k):
    i, j, res = 0, len(arr) - 1, 0
    nums.sort()

    while i < j:
        if nums[i] + nums[j] < k:
            res = max(res, nums[i] + nums[j])
            i += 1
        else:
            j -= 1
    return res

# N + M


def addTwoNumbers1(l1, l2):
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)

        result_tail.next = ListNode(out)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next

# N + M


def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s1, s2 = 0, 0

    while l1 != None:
        s1 = s1*10+l1.val
        l1 = l1.next

    while l2 != None:
        s2 = s2*10+l2.val
        l2 = l2.next

    dummylist = dummy = ListNode(0)

    for i in str(s1+s2):
        dummy.next = ListNode(i)
        dummy = dummy.next

    return dummylist.next

# N ^ 2


def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = float('inf')

    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                return sum

            if abs(sum - target) < abs(result - target):
                result = sum

            if sum < target:
                j += 1

            elif sum > target:
                k -= 1
    return result

# N


def sortArrayByParity(self, A):
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 > A[j] % 2:
            A[i], A[j] = A[j], A[i]

        if A[i] % 2 == 0:
            i += 1
        if A[j] % 2 == 1:
            j -= 1

    return A


# amount * num of subproblems per amount
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[-1] == float('inf'):
        return -1
    return dp[-1]


def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
    m, n = len(board), len(board[0])
    stable = False

    while True:
        stable = True
        crush = set()
        for i in range(m):
            for j in range(n - 2):
                if board[i][j] == board[i][j + 1] == board[i][j + 2] != 0:
                    stable = False
                    crush.update([(i, j), (i, j + 1), (i, j + 2)])

        for i in range(m - 2):
            for j in range(n):
                if board[i][j] == board[i + 1][j] == board[i + 2][j] != 0:
                    stable = False
                    crush.update([(i, j), (i + 1, j), (i + 2, j)])

        if stable:
            return board

        for x, y in crush:
            board[x][y] = 0

        for j in range(n):
            offset = 0
            for i in range(m - 1, -1, -1):
                k = i + offset
                if (x, y) in crush:
                    offset += 1
                else:
                    board[k][y] = board[x][y]

            for x in range(offset):
                board[x][y] = 0
