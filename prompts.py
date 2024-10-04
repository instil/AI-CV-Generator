existing_cv = """
    <cv>
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
    Technologies: AWS, NetSuite, React, Apache Camel, Java, React, Redux.
    </cv>"""

additional_context = """
    <context>
    - Other certifications: AWS Solutions Architect, AWS Hero
    - Current company position: Principal Software Engineer
    - Bio considerations: Engineer with 50 years of experience in developing both front-end and back-end serverless solutions. Has led multiple AWS and Azure cloud projects.
    </context>
    """

PROMPT = """
You are acting as a salesperson for a software development consultancy. Your task is to use and existing CV of an employee and any other additional provided context to create a compelling, client-focused, and results-driven CV to be sent to a potential client. 

Use the following set of steps as a guide for generating the CV
1. Take the existing provided CV between the tags <cv></cv> use this as a base for the final CV
2. Use the provided additional context to update the provided CV in places that require it. This could include things like updating job role, bio, skills and experience
3. When processing the work experience sections, you might notice that there is no date, if that happens and it is a start date missing then dateStart in the json should be null, if an end date is missing then the dateEnd in the json should be null
4. Make the CV sound professional and compelling
5. Summarize sections where it makes sense without losing context
6. Use the final CV to populate a JSON template provided between the tags <json></json>
7. Ensure the json is valid against the provided schema if not update accordingly, remember dates that aren't provided in 
    the experience section can be left as null or empty strings in the final json.

The final output should meet the following requirements:
1. The provided existing CV could be outdated update the final CV must have been updated where necessary.
2. The entire response should contain only valid JSON.
3. The word count of the entire CV (including all fields) must not exceed 500 words.
4. Only one CV should be generated.
5. If there is no dates mentioned for any work experience in the provided CV then `dateStart` and `dateEnd` should be left null or empty.
6. The final CV must be structured using the specific JSON format provided below.

Here is the required JSON template for the CV
<json>
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
}
<json>

    Below is the additional context and the engineer's existing outdated CV that you should consider when generating the final CV.

Additional Context:
""" + additional_context + """

Existing CV:
""" + existing_cv + """

Please now generate the CV as JSON considering everything previously provided.
"""
