from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

class IA:
    def __init__(self):
        model_name = 'gpt2'
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
    
    def generate_responses(self, text, max_length=500):
        # Encode le texte d'entrée
        encoded_input = self.tokenizer.encode(text, return_tensors='pt')
        # Génère une suite de texte
        output_sequences = self.model.generate(
            input_ids=encoded_input,
            max_length=max_length,
            temperature=1.0,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2,
            do_sample=True,
            num_return_sequences=1
        )
        # Décode la sortie générée en texte
        generated_text = self.tokenizer.decode(output_sequences[0], skip_special_tokens=True)
        
        return generated_text