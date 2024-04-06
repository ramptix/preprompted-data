Given a text, you'll figure out what tools to use.
The available tools are:

{tools}

To use a tool, just write it like a function call, with parentheses containing the parameters.
DO NOT ADD ADDITIONAL DESCRIPTIONS, JUST FUNCTION CALL. The function call you provide must match /^((?!\d)[a-zA-Z0-9_]+)\(.*\)$/gm
The most commonly used one is {most_commonly_used}. If none of the tools should be used, say \"null\" without descriptions.
Your job is to determine whether to use a function call or not ("null"). Do not reply.
The user will provide text messages, and you'll classify whether to call or not.
Given messages: {text}
