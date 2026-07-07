from langchain_core.prompts import PromptTemplate
blog_prompt=PromptTemplate(
    input_variables=["topic","tone","length","audience"],
    template="""
you are an expert content writer.

write a {length} blog post.
Topic: {topic}
Tone: {tone}
Audience: {audience}

Include:
- Catchy Title
- Introduction
- 4-5 headings
- Practical examples
- Conclusion
- key takeaways

Return the response in Markdown.
"""

)