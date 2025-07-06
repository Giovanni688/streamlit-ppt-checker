import boto3
from botocore.exceptions import ClientError
import re

def filter_objective_statements(texts):
    """Filter out objective statements from a list of texts."""
    objective_statements = []
    for text in texts:
        # Simple heuristic: Keep sentences that contain numbers, dates, or factual keywords
        if re.search(r"\b\d{1,4}\b", text) or re.search(r"\b(year|percent|data|study|report|fact|evidence)\b", text, re.IGNORECASE):
            objective_statements.append(text)
    return objective_statements

def check_factual_accuracy(fact):
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    model_id = "amazon.nova-lite-v1:0"
    
    usermassage = "ファクトチェックしてください："
    text = usermassage + fact

    # Prepare the conversation with the user message
    conversation = [
        {
            "role": "user",
            "content": [{"text": text}],
        }
    ]

    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
        )

        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        return f"ERROR: Can't invoke '{model_id}'. Reason: {e}"

def process_and_check_facts(texts):
    """Process extracted texts and check factual accuracy."""
    # Filter objective statements
    objective_statements = filter_objective_statements(texts)
    
    # Perform fact-checking on each statement
    results = {}
    for statement in objective_statements:
        results[statement] = check_factual_accuracy(statement)
    
    return results

def estimate_api_cost(texts, tokens_per_call=150, cost_per_1000_tokens=0.00006):
    """
    Estimate the cost of API calls to AWS Bedrock.

    Args:
        texts (list): List of extractsed texts to process.
        tokens_per_call (int): Average number of tokens per API call (input + output).
        cost_per_1000_tokens (float): Cost per 1,000 tokens for the API.

    Returns:
        float: Estimated total cost of API calls.
    """
    # Calculate total tokens
    total_tokens = len(texts) * tokens_per_call
    
    # Calculate total cost
    total_cost = (total_tokens / 1000) * cost_per_1000_tokens
    
    return total_cost