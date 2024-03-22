from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

class IA:
    def __init__(self, cache_dir="./.cache"):
        model_name = 'DracolIA/BERT-Context-based-QA'
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name, cache_dir=cache_dir)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def generate_responses(self, question, file_content, have_file):
        
        if have_file:
            context = file_content
        else:   
            context = ""
    
        # Tokenize the input question and context
        inputs = self.tokenizer.encode_plus(
            question, context,
            add_special_tokens=True,
            return_tensors="pt",
            truncation="only_second",  # Only truncate the context, not the question
            max_length=512,
            stride=128,
            return_overflowing_tokens=True,
            return_offsets_mapping=True,
            padding="max_length"
        )

        input_ids = inputs["input_ids"].to(self.device)
        attention_mask = inputs["attention_mask"].to(self.device)

        # Model inference
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)

        # Get the most likely beginning and end of answer with the argmax of the score
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits

        answer_start = torch.argmax(answer_start_scores, dim=-1)  # Get the index of the highest start score
        answer_end = torch.argmax(answer_end_scores, dim=-1) + 1  # Get the index of the highest end score

        # Convert the token indexes to actual text of the answer
        answer = self.tokenizer.decode(inputs['input_ids'][0][answer_start:answer_end], skip_special_tokens=True)

        #print(input_ids)
        print("Answer start : ", answer_start)
        print("Answer end : " , answer_end)
        print(self.tokenizer.decode(input_ids[0][answer_end:answer_start]))
        return answer

