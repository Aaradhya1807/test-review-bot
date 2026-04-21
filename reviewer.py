import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(code_diff: str) -> str:
    prompt = f"""You are an expert code reviewer. Review the following code diff and provide feedback on:
1. Bugs or logic errors
2. Security issues
3. Code quality & readability
4. Performance improvements

Be concise, specific, and constructive. Format your response with clear sections.

Code diff:
{code_diff}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Test with a dummy diff
    test_diff = """
    + def get_user(id):
    +     query = f"SELECT * FROM users WHERE id = {id}"
    +     return db.execute(query)
    """
    print(review_code(test_diff))