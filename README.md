This Flask App uses a Pretrained model on English language using a causal language modeling (CLM) objective https://huggingface.co/gpt2. The model takes an input of a view words and generates a text of up to 300 words. The docker image is deploayed on https://text-generator.azurewebsites.net/

The startup takes a few minutes due to the init of the GPT2Tokenizer at the start. Also every request take a view a seconds.

Docker run command: docker run -d -p 5111:5000 ds20m017/text-generator