from utils.openai import OpenAI


def test_parse_resp():
    openai = OpenAI()
    mock_resp = {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "As an AI language model, I do not have a name but you may refer to me as OpenAI Language Model.",
                    "role": "assistant",
                },
            }
        ],
        "created": 1682096483,
        "id": "chatcmpl-77oQN6NeTQGPkaMRP26suutCbWtB7",
        "model": "gpt-3.5-turbo-0301",
        "object": "chat.completion",
        "usage": {"completion_tokens": 24, "prompt_tokens": 12, "total_tokens": 36},
    }

    expected_result = "As an AI language model, I do not have a name but you may refer to me as OpenAI Language Model."

    assert openai._parse_response(mock_resp) == expected_result
