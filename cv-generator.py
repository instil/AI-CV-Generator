
if __name__ == '__main__':
    from haystack_integrations.components.generators.llama_cpp import LlamaCppGenerator

    generator = LlamaCppGenerator(
        model="openchat-3.5-1210.Q3_K_S.gguf",
        n_batch=128,
        n_ctx=2048,
        generation_kwargs={"max_tokens": 500, "temperature": 0.1},
    )
    generator.warm_up()
    prompt = f"I will be using you to extract and build a cv using an existing cv and other context, I will be providing information I want you keep in mind for whenever you generate the CV at the end whilst. The format or CV template I want you to keep in mind is the following block of text in single quotes : \n" \
             f"‘Persons Name here \n Position in company here \n Bio - content here \n Skills - content here \n Certifications - content here\nProjects and previous experiences -\nCompany/project - experience content here’\nI am now going to provide some additional context which I want you to consider when generating the final CV. Other certifications - AWS solutions Architect, AWS hero. Company position is currently principal software engineer. Other things to consider for bio - engineer has now 50 years of experience, developing both front end and backend serverless solutions. Lead multiple AWS and Azure cloud projects.\nBelow in single quotes is the engineers existing outdated CV I want to be considered and used as reference for building the finalised CV after considering everything.\n‘Jim Bob" \
             f"\nSenior Software Engineer" \
             f"\nBio - A Senior Software Engineer with over 6 years experience across many team-based projects and successful implementations. Proficient in AWS services like API Gateway, Lambda and DynamoDB. Skilled in NodeJS, microservices and Serverless tech. Excels in client communications, project leadership and adeptly translates business needs into technical solutions. Experienced in Agile and SCRUM delivery." \
             f"\nSkills - Java, Docker, NodeJS, Oracle NetSuite, AWS, DynamoDB, Lambda, S3, Angular, React, Apache Camel, Modern Project Management Methodologies (Agile, SCRUM, Kanban), CI/CD (BitBucket Pipelines)." \
             f"\nCertifications - Oracle NetSuite Foundation Certified\n" \
             f"\nProjects Experience -\n" \
             f"\n* companyI/V Senior Software Engineer - Built an application for business product validation, concentrating on both backend (using Java, Ruby, Docker, and Postgres) and frontend (with Ruby on Rails & React), and integrating with cloud-based microservices on AWS." \
             f"\n" \
             f"\nTechnologies: Java, Ruby, Docker, Postgres, React, AWS\n" \
             f"\n* companyI/J Senior Software Engineer - Responsible for maintaining and enhancing an established support portal application. This application consists of a Java backend and an Angular frontend, entirely hosted on AWS." \
             f"\n" \
             f"\nTechnologies: AWS, Java, Angular\n" \
             f"\n" \
             f"\n* company3 Senior Software Engineer - Built end-to-end development of E-Commerce, 3PL, Shipping, Financial & bespoke integrations and apps, from scoping, requirements gathering and client engagement to architecting, development, and support. Led the transition and development of our in-house integration platform within AWS. Built bespoke integrations with NetSuite and third party systems. Developed customisations for clients' NetSuite systems. R&D of in-house frameworks, systems and applications." \
             f"\n" \
             f"\nTechnologies: AWS, NetSuite, React, Apache Camel, Java, React, Redux.’" \
             f"\n" \
             f"\nCan you generate a CV considering everything."
    result = generator.run(prompt)
    print(result["replies"][0])

