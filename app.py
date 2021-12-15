from flask import Flask, request, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2') 
model = GPT2LMHeadModel.from_pretrained('gpt2', pad_token_id = tokenizer.eos_token_id)
text = 'What is love'

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('input.html', defaultText = text, resultText = '')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['InputTextField']
    encoded_input = tokenizer.encode(text, return_tensors='pt')
    output = model.generate(encoded_input, max_length = 300, num_beams = 1, no_repeat_ngram_size = 1, do_sample=True, early_stopping = True)
    resultText = tokenizer.decode(output[0], skip_special_tokens = True)
    return render_template('input.html', defaultText = text, resultText = resultText)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)