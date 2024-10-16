def find_smaller_number(a, b):
    if a < b:
        return a
    else:
        return b

def calculate_total_price(width, length, location):
    # set price
    Poly_Large = 80
    Poly_Small = 60
    #get smallest
    Small_Width = find_smaller_number(width, length)
    #check board size
    if Small_Width > 120:
        Small_Width = Small_Width / 2
        if width <= 120:
            material_price = width * price_per_cm * 2
    else:
        if Small_Width > 60:
            material_price = Small_Width * Poly_Large
        if Small_Width <= 60:
            material_price = Small_Width * Poly_Small

    # 材料價格計算

    # 運費和工費
    labor_cost = 5000
    shipping_cost = {
        "臺北新北": 3000,
        "桃園": 3500,
        "新竹": 4500,
        "宜蘭": 4500,
        "臺中/苗栗": 5000
    }

    # 檢查地點是否合法
    if location not in shipping_cost:
        raise ValueError(f"地點 {location} 無效。請選擇有效的地點: {', '.join(shipping_cost.keys())}")

    # 總價計算
    total_price = material_price + labor_cost + shipping_cost[location]
    return total_price

# 示例
width = float(input("請輸入寬度 (cm): "))
length = float(input("請輸入長度 (cm): "))
location = input("請輸入地點 (臺北新北, 桃園, 新竹, 臺中/苗栗): ")238

total_price = calculate_total_price(width, length, price_per_cm, location)
print(f"總價: {total_price}")
