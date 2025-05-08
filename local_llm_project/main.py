from transformers import AutoModelForCausalLM, AutoTokenizer
import os

def load_prompt(file_path):
    """Load a prompt from a file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    else:
        print(f"File not found: {file_path}")
        return None

def main():
    model_name = "gpt2"  
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    print("Choose an option:")
    print("1. Enter a prompt manually")
    print("2. Load a prompt from a file")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        prompt = input("Enter a prompt: ")
    elif choice == "2":
        file_path = input("Enter the file path: ")
        prompt = load_prompt(file_path)
        if not prompt:
            return
    else:
        print("Invalid choice. Exiting.")
        return

    print("Generating text...")
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()