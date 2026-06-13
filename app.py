from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def simple_linear_regression(points, predict_x):
    """Hitung regresi linear sederhana y = a + bx.

    points: list berisi dict {"x": modal, "y": keuntungan}
    predict_x: modal yang ingin diprediksi
    return: dict berisi a, b, y
    """
    if len(points) < 3:
        raise ValueError("Minimal butuh 3 data penjualan.")

    clean_points = []
    for point in points:
        x = float(point["x"])
        y = float(point["y"])
        if x < 0 or y < 0:
            raise ValueError("Modal dan keuntungan tidak boleh negatif.")
        clean_points.append({"x": x, "y": y})

    predict_x = float(predict_x)
    if predict_x < 0:
        raise ValueError("Modal prediksi tidak boleh negatif.")

    n = len(clean_points)
    sum_x = sum(point["x"] for point in clean_points)
    sum_y = sum(point["y"] for point in clean_points)
    sum_xy = sum(point["x"] * point["y"] for point in clean_points)
    sum_x2 = sum(point["x"] ** 2 for point in clean_points)

    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        raise ValueError("Modal tiap hari tidak boleh sama semua, karena garis regresi tidak bisa dihitung.")

    b = (n * sum_xy - sum_x * sum_y) / denominator
    a = (sum_y - b * sum_x) / n
    y = a + b * predict_x

    return {"a": a, "b": b, "y": y}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    try:
        result = simple_linear_regression(
            points=data.get("points", []),
            predict_x=data.get("predict_x", 0),
        )
        return jsonify(result)
    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
