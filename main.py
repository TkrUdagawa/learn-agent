import anthropic


def main():
    # AnthropicBedrockは ~/.aws/credentials の認証情報を自動で使用する
    client = anthropic.AnthropicBedrock(
        aws_region="ap-northeast-1",
    )

    message = client.messages.create(
        model="jp.anthropic.claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "日本語で自己紹介してください。"}
        ],
    )

    print(message.content[0].text)


if __name__ == "__main__":
    main()
