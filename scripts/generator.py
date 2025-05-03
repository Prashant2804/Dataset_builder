import requests
import os

def generate_images(prompt, count, api_url='http://localhost:8000/generate'):
    response = requests.post(api_url, json={'prompt': prompt, 'count': count})
    
    if response.status_code == 200:
        images = response.json().get('images', [])
        save_generated_images(images, prompt)
    else:
        print(f"Error: {response.status_code} - {response.text}")

def save_generated_images(images, prompt):
    output_dir = f"data/generated/{prompt}/"
    os.makedirs(output_dir, exist_ok=True)
    
    for idx, image_data in enumerate(images):
        image_path = os.path.join(output_dir, f"{prompt}_{idx}.png")
        with open(image_path, 'wb') as img_file:
            img_file.write(image_data)
    
    print(f"Generated {len(images)} images for prompt '{prompt}' and saved to '{output_dir}'.")

if __name__ == "__main__":
    prompt = input("Enter the prompt for image generation: ")
    count = int(input("Enter the number of images to generate: "))
    generate_images(prompt, count)