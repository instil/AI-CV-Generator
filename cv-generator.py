
if __name__ == '__main__':
    # Use a pipeline as a high-level helper
    from transformers import pipeline

    # pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B")
    from haystack_integrations.components.generators.llama_cpp import LlamaCppGenerator

    generator = LlamaCppGenerator(
        model="openchat-3.5-1210.Q3_K_S.gguf",
        n_batch=128,
        n_ctx=2048,
        generation_kwargs={"max_tokens": 500, "temperature": 0.1},
    )


    # loads of don'ts
    #
    generator.warm_up()
    prompt = """
    I will be using you to extract and build a CV using an existing CV and additional context. Please ensure the final CV is generated in the specific format provided below. The format or CV template I want you to follow is:
    ‘[Person's Name here]
    [Position in company here]
    Bio: [content here]
    Skills: [content here]
    Certifications: [content here]
    Projects and previous experiences:
    - [Company/project] - [experience content here]’

    I am now going to provide some additional context which I want you to consider when generating the final CV.

    Additional Context:
    - Other certifications: AWS Solutions Architect, AWS Hero
    - Current company position: Principal Software Engineer
    - Bio considerations: Engineer with 50 years of experience in developing both front-end and back-end serverless solutions. Has led multiple AWS and Azure cloud projects.

    Below, in single quotes, is the engineer's existing outdated CV. Use this as a reference for building the final CV after considering everything.

    ‘Jim Bob
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
    Technologies: AWS, NetSuite, React, Apache Camel, Java, React, Redux.’

    Can you generate a CV considering all the provided information and context?
    """

    result = generator.run(prompt)
    # result = pipe(prompt)
    print(result)

