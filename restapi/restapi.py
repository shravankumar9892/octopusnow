DIST_PACKAGES = '/content/gdrive/My Drive/octopusnow/data/dist-packages'
DRIVE_FILES = '/content/gdrive/My Drive/octopusnow/data'
CURRENT_DIR = '/content/'
PREFIX_PATH = '/content/gdrive/My Drive/octopusnow/data/dist-packages'
pretrained_path = DRIVE_FILES + '/BioBertFolder/biobert_v1.0_pubmed_pmc/'
# ffn_weight_file = None
bert_ffn_weight_file = DRIVE_FILES + '/newFolder/models/bertffn_crossentropy/bertffn'
embedding_file = DRIVE_FILES + '/Float16EmbeddingsExpanded5-27-19.pkl'

from docproduct.predictor import RetreiveQADoc
from flask import Flask, jsonify, json, request
from flask_ngrok import run_with_ngrok
from google.colab import drive
drive.mount('/content/gdrive')

app = Flask(__name__)
run_with_ngrok(app)

def load_model():
    global doc
    doc = RetreiveQADoc(pretrained_path=pretrained_path,
                        ffn_weight_file=None,
                        bert_ffn_weight_file=bert_ffn_weight_file,
                        embedding_file=embedding_file)

@app.route('/', methods=['POST'])
def octopusnow():
    if request.method == 'POST':
        talk = request.json
        returnedanswers = doc.predict( list(talk.values())[0], search_by='answer', topk=10, answer_only=False)
        return jsonify({"octoreport":returnedanswers})

if __name__ == '__main__':
    print(("* Loading Octopus Now model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run()
