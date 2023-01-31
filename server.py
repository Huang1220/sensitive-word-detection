from flask import Flask, request
import json
import check

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>违规词敏感词检测系统</h1></br>作者：Neutron_star"

@app.route("/api/check", methods=["POST", "GET"])
def check_sentences():
    data = request.values
    if data:
        sentence = data.get("input")
        if sentence:
            return json.dumps(check.check_words(sentence), ensure_ascii=False)
        else:
            return json.dumps({"code" : 404, "message" : "在传入数据加上input字段，请检查"}, ensure_ascii=False)
    else:
        return json.dumps({"code" : 404, "message" : "在传入数据加上input字段，请检查"}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
