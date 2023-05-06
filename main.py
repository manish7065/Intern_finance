from flask import Flask, request, render_template,Response
from finance.entity.artifact_entity import StockSelection
from finance.pipeline import TrainPipeline
from finance.exception import FinanceException

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        data = request.form
        option = data["options"]
        StockSelection.stock_selected = option
        print(f'getting the data: {option}')

        trian_pipeline = TrainPipeline()
        if trian_pipeline.is_pipeline_running:
            return Response("Training pipeline is running")
        trian_pipeline.run_pipeline()

        return render_template("result.html", option=option)
    except Exception as e:
        return Response(f" Error ocuured! {e}")
        raise FinanceException(e, sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
