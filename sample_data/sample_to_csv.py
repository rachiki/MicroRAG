import csv

def load_qa_pairs(file_path, output_csv):
    qa_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        next(f)  # Skip header
        for line in f.readlines():
            parts = line.strip().split('\t')
            if len(parts) == 6:
                article_title, question, answer, diff_q, diff_a, article_file = parts

                # We always have a question and an answer, but repeated twice for every question
                # This just kicks out any NULL answer, if we have two valid answers, we take the second one
                if answer != 'NULL':
                    qa_dict[question] = answer
    
    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question', 'Answer'])  # Write header
        for question, answer in qa_dict.items():
            writer.writerow([question, answer])

    print(f"Saved {len(qa_dict)} QA pairs to '{output_csv}'")
    return qa_dict

def main():
    file_path = 'sample_data/S08_question_answer_pairs.txt'
    output_csv = 'data/sample_qa_pairs.csv'
    qa_dict = load_qa_pairs(file_path, output_csv)

if __name__ == "__main__":
    main()
