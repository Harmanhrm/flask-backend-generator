from flask import Flask, jsonify, request
from flask_cors import CORS
from backtracking_generator import BacktrackingGenerator  # Adjust import according to your setup

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/generate_maze', methods=['GET'])
def generate_maze():
    size = int(request.args.get('size', 10))  # Default size is 10
    generator = BacktrackingGenerator(size)
    generator.generate_maze()
    maze = generator.grid.tolist()  # Convert numpy array to list
    steps = generator.steps
    return jsonify({"maze": maze, "steps": steps})

if __name__ == '__main__':
    app.run(debug=True)
