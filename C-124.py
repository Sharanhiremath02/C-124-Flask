from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[{
    "id":1,
    "title":u"buy vegetables",
    "description":u"carrot,brinjal,tomato,potato,onion",
    "done":False
},
{
    "id":2,
    "title":u"buy grocery",
    "description":u"toor dal,atta,rice,tea powder",
    "done":False
}]
@app.route("/")
def hello_world():
    return "hello welcome to python programing"

@app.route("/getdata")
def get_task():
    return jsonify({
        "data":tasks
    })

@app.route("/adddata",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the information"

        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added" 
    })        

if(__name__ == "_main_"):
    app.run(debug=True)

app.run(debug=True)