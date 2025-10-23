def count_ways(n):
    # Trường hợp đặc biệt
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    # Tạo mảng dp để lưu số cách tại mỗi bậc
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # Quy hoạch động: mỗi bậc = tổng 2 bậc trước
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# --- Gọi hàm ---
n = int(input("Nhập số bậc thang: "))
print("Số cách đi lên bậc", n, "là:", count_ways(n))
