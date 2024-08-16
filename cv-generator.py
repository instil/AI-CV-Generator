import logging

if __name__ == '__main__':
    from haystack_integrations.components.generators.llama_cpp import LlamaCppGenerator

    generator = LlamaCppGenerator(
        model="openchat-3.5-1210.Q4_0.gguf",
        n_batch=128,
        n_ctx=4096,
        generation_kwargs={"max_tokens": 2500, "temperature": 0.1},
    )

    # logging.basicConfig(level=logging.CRITICAL)
    # logging.getLogger('llama_new_context_with_model').setLevel(logging.CRITICAL)
    # llama_logger = logging.getLogger('LlamaCppGenerator')
    # llama_logger.setLevel(level=logging.CRITICAL)
    # haystack_logger = logging.getLogger('haystack')
    # haystack_logger.setLevel(level=logging.CRITICAL)

    existing_cv = """
    Jim Bob
    Senior Software Engineer
    Bio: A Senior Software Engineer with over 6 years experience across many team-based projects and successful implementations. Proficient in AWS services like API Gateway, Lambda and DynamoDB. Skilled in NodeJS, microservices and Serverless tech. Excels in client communications, project leadership and adeptly translates business needs into technical solutions. Experienced in Agile and SCRUM delivery.
    Skills: Java, Docker, NodeJS, Oracle NetSuite, AWS, DynamoDB, Lambda, S3, Angular, React, Apache Camel, Modern Project Management Methodologies (Agile, SCRUM, Kanban), CI/CD (BitBucket Pipelines).
    Certifications: Oracle NetSuite Foundation Certified
    Projects Experience:
    - Company 1 Senior Software Engineer - Built an application for business product validation, concentrating on both backend (using Java, Ruby, Docker, and Postgres) and frontend (with Ruby on Rails & React), and integrating with cloud-based microservices on AWS.
    Technologies: Java, Ruby, Docker, Postgres, React, AWS
    - Company 2 Senior Software Engineer - Responsible for maintaining and enhancing an established support portal application. This application consists of a Java backend and an Angular frontend, entirely hosted on AWS.
    Technologies: AWS, Java, Angular
    - Company 3 Senior Software Engineer - Built end-to-end development of E-Commerce, 3PL, Shipping, Financial & bespoke integrations and apps, from scoping, requirements gathering and client engagement to architecting, development, and support. Led the transition and development of our in-house integration platform within AWS. Built bespoke integrations with NetSuite and third party systems. Developed customisations for clients' NetSuite systems. R&D of in-house frameworks, systems and applications.
    Technologies: AWS, NetSuite, React, Apache Camel, Java, React, Redux."""

    additional_context = """
    - Other certifications: AWS Solutions Architect, AWS Hero
    - Current company position: Principal Software Engineer
    - Bio considerations: Engineer with 50 years of experience in developing both front-end and back-end serverless solutions. Has led multiple AWS and Azure cloud projects.
    """

    generator.warm_up()
    prompt = """
You are acting as a salesperson for a software development consultancy. Your task is to create a compelling, client-focused, and results-driven CV for a potential client using an employee's existing CV and additional context provided.

The final CV should meet the following requirements:
1. It must be structured in the specific JSON format provided below.
2. The entire response should contain only valid JSON.
3. The word count of the entire CV (including all fields) must not exceed 500 words.
4. Only one CV should be generated using the provided template.
5. If there is no dates mentioned for any work experience in provided CV then `dateStart` and `dateEnd` should be null or empty.

Here is the required JSON template for the CV (ensure your output matches this format exactly):
```json
{
    "name": "string",
    "jobRole": "string",
    "bio": "string",
    "skills": "string",
    "experience": [
        {
            "companyName": "string",
            "jobRole": "string",
            "dateStart": "Date",
            "dateEnd": "Date",
            "description": "string",
            "technologies": ["string"]
        }
    ]
}```

    Below is the additional context and the engineer's existing outdated CV that you should consider when generating the final CV.

Additional Context:
""" + additional_context + """

Existing CV:
""" + existing_cv + """

Please generate the final CV in JSON format considering all the provided information and context.
"""

    result = generator.run(prompt)
    print(result["replies"][0])
    # print(result)