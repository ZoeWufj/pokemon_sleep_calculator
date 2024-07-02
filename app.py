from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 定義食譜
recipes = {
    "curry": {
        "煉獄玉米乾咖哩": {"火辣香草": 27, "豆製肉": 24, "萌綠玉米": 14, "暖暖薑": 12},
        "絕對睡眠奶油咖哩": {"窩心洋芋": 18, "好眠番茄": 15, "放鬆可可": 12, "哞哞鮮奶": 10},
        "炙燒尾肉咖哩": {"美味尾巴": 8, "火辣香草": 25},
        "忍者咖哩": {"萌綠大豆": 15, "豆製肉": 9, "粗枝大蔥": 9, "品鮮蘑菇": 5},
    },
    "salad": {
        "忍者沙拉": {"萌綠大豆": 15, "暖暖薑": 11, "粗枝大蔥": 15, "品鮮蘑菇": 12},
        "萌綠沙拉": {"純粹油": 22, "萌綠玉米": 17, "好眠番茄": 14, "窩心洋芋": 9},
        "呆呆獸尾巴的胡椒沙拉": {"美味尾巴": 10, "火辣香草": 10, "純粹油": 15},
        "冥想香甜沙拉": {"特選蘋果": 21, "甜甜蜜": 16, "萌綠玉米": 12},
    },
    "dessert": {
        "花之禮馬卡龍": {"放鬆可可": 25, "特選蛋": 25, "甜甜蜜": 17, "哞哞鮮奶": 10},
        "茶會玉米司康": {"特選蘋果": 20, "萌綠玉米": 18, "暖暖薑": 20, "哞哞鮮奶": 9},
        "胖丁百匯布丁": {"甜甜蜜": 20, "特選蛋": 15, "哞哞鮮奶": 10, "特選蘋果": 10},
        "大爆炸爆米花": {"萌綠玉米": 15, "純粹油": 14, "哞哞鮮奶": 7},
    }
}

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    selected_recipes = data.get('recipes', [])
    total_ingredients = {}

    for recipe in selected_recipes:
        for category, category_recipes in recipes.items():
            if recipe in category_recipes:
                for ingredient, amount in category_recipes[recipe].items():
                    if ingredient in total_ingredients:
                        total_ingredients[ingredient] += amount
                    else:
                        total_ingredients[ingredient] = amount

    return jsonify(total_ingredients)

if __name__ == '__main__':
    app.run(debug=True)
