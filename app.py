from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_flames(name1, name2):
    """Calculate FLAMES result with improved letter counting logic"""
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    list1 = list(name1)
    list2 = list(name2)
    
    # Remove common letters - handle multiple occurrences
    for letter in list(set(list1)):  # Use set to iterate unique letters
        if letter in list2:
            # Count the minimum number of times the letter appears in both lists
            min_count = min(list1.count(letter), list2.count(letter))
            
            # Remove that number of occurrences from BOTH lists
            for _ in range(min_count):
                list1.remove(letter)
                list2.remove(letter)
    
    count = len(list1) + len(list2)
    flame_list = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sister']
    
    # Eliminate from FLAMES list using count
    while len(flame_list) > 1:
        index = (count - 1) % len(flame_list)
        flame_list.pop(index)
    
    return flame_list[0], count

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    name1 = data.get('name1', '').strip()
    name2 = data.get('name2', '').strip()
    
    if not name1 or not name2:
        return jsonify({'error': 'Please enter both names'}), 400
    
    try:
        result, count = calculate_flames(name1, name2)
        return jsonify({'result': result, 'count': count, 'name1': name1.title(), 'name2': name2.title()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
