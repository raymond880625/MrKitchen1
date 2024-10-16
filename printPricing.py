def calculate_financials(numbers):
    # Calculate the total sum of the numbers
    total = sum(numbers)
    
    # Calculate the breakdown
    deposit = round(total * 0.1)
    order = round(total * 0.4)
    shipment = total - order - deposit
    
    # Create the formatted output
    result = f"總共：{' + '.join([f'{n:.2f}' for n in numbers])} = {total:.2f}\n"
    result += f"定金：{deposit:.0f}（10%）\n"
    result += f"下單：{order:.0f}（40%）\n"
    result += f"出貨：{shipment:.0f}（50%）\n"
    
    return result

# Input section
try:
    input_numbers = input("請輸入數字，使用逗號分隔: ")
    numbers = [float(num) for num in input_numbers.split(",")]
    output = calculate_financials(numbers)
    print(output)
except ValueError:
    print("請確保所有輸入的數字都是有效的數字。")

