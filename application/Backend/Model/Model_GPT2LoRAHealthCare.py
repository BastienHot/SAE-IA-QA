import keras
import keras_nlp
import tensorflow as tf

class GPT2LoRAHealthCare:

    """
    #model_name = "DracolIA/GPT-2-LoRA-HealthCare"
    model_name = "LoRA_Model_CP3.keras"
    model = keras.models.load_model(model_name)

    def clean_answer_text(text: str) -> str:
        # Define the start marker for the model's response
        response_start = text.find("[ANSWER]") + len("[ANSWER]")

        # Extract everything after "Doctor:"
        response_text = text[response_start:].strip()
        last_dot_index = response_text.rfind(".")
        if last_dot_index != -1:
            response_text = response_text[:last_dot_index + 1]

        # Additional cleaning if necessary (e.g., removing leading/trailing spaces or new lines)
        response_text = response_text.strip()

        return response_text


    def generate_responses(self, question):
        prompt = f"[QUESTION] {question} [ANSWER]"
        output = self.model.generate(prompt, max_length=1024)
        # Clean and extract the model's response from `output`
        return GPT2LoRAHealthCare.clean_answer_text(output)
    """

    def generate_responses(question):
        return "Reponse chatbot : " + question