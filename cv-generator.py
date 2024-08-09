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
    You are taking on the role of a sales person in a software development consultancy business, you need to use employee CVs and extra information in order to build a compelling CV to send to potential clients. The final CV should be client focused and results driven. 
    Please ensure the final response has a total word count of less than or equal to 500, and is generated in the specific JSON format provided below, your response should contain only valid JSON. Please generate only one CV using the following template:
    {
        name: string,
        jobRole: string,
        bio: string,
        skills: string,
        experience: [{
            companyName: string,
            jobRole: string,
            dateStart: Date,
            dateEnd: Date,
            description: string,
            technologies: string[]
        }]
    }

    This is the end of the JSON template.

    The following are 3 examples of a good responses, please use them to follow for formatting but not for content:

    Example 1:

    {
        "name": "Stephen McMillan",
        "jobRole": "Senior iOS Engineer",
        "bio": "Senior mobile engineer with 5 years experience building mobile applications for some of the largest point of sale and online ordering experiences used by customers across the USA. Particularly proficient designing and building iOS applications.",
        "skills": "iOS development using UIKit, Combine, CoreData, and AutoLayout. Debugging with Instruments and Xcode Memory Graph Debugger. Unit Testing and UI Testing with XCTest, Quick, Nimble, and Appium.",
        "experience": [
            {
                "companyName": "Slice",
                "jobRole": "Senior iOS Engineer",
                "dateStart": "January 2021",
                "dateEnd": "April 2024",
                "description": "Introduced exploratory testing sessions and spearheaded improvements in the PR review process to greatly enhance the stability of the platform for shop partners.  Updated client syncing solution from basic polling to increase speed, improve reliability and reduce costs to the business by using web-sockets. Integrated a legacy Objective-C point of sale with Slice backend services and fully restyled following acquisition of this product. Led a significant number of core features from planning to delivery in order to drive adoption of the Slice Register POS product.",
                "technologies": [
                    "UIKit",
                    "Combine",
                    "CoreData",
                    "SwiftUI",
                    "AWS Amplify",
                    "Xcode Memory Graph Debugger"
                ]
            },
            {
                "companyName": "Shopkeep",
                "jobRole": "iOS Engineer",
                "dateStart": "March 2019",
                "dateEnd": "December 2020",
                "description": "Extensively led a project migrating 25,000 active installations from a peer-to-peer iPad data sync to a robust AWS solution, enhancing reliability and facilitating web-based customer orders. Engineered features addressing business needs amidst the COVID-19 pandemic, including Pay by Link/QR Code and online ordering functionalities. Played a pivotal role in automating the bi-weekly release process through the development of a Slack bot, streamlining branch management, build triggering, and stakeholder communication. Significantly refactored extensive Objective-C codebases into meticulously tested, contemporary Swift implementations.",
                "technologies": [
                    "AWS",
                    "Combine",
                    "SwiftUI",
                    "XCTest",
                    "Quick",
                    "Nimble",
                    "Appium"
                ]
            }
        ]
    }

    Example 2: 

    {
        "name": "Sam McKnight",
        "jobRole": "Senior Software Engineer",
        "bio": "A Senior Software Engineer with over 6 years experience across many team-based projects and successful implementations. Proficient in AWS services like API Gateway, Lambda and DynamoDB. Skilled in NodeJS, microservices and Serverless tech. Excels in client communications, project leadership and adeptly translates business needs into technical solutions. Experienced in Agile and SCRUM delivery.",
        "skills": "Java, Docker, NodeJS, Oracle NetSuite, AWS, DynamoDB, Lambda, S3, Angular, React, Apache Camel, Modern Project Management Methodologies (Agile, SCRUM, Kanban), CI/CD (BitBucket Pipelines).",
        "experience": [
            {
                "companyName": "Vypr",
                "jobRole": "Senior Software Engineer",
                "dateStart": "January 2023",
                "dateEnd": "April 2024",
                "description": "Built an application for business product validation, concentrating on both backend (using Java, Ruby, Docker, and Postgres) and frontend (with Ruby on Rails & React), and integrating with cloud-based microservices on AWS.",
                "technologies": [
                    "Java", 
                    "Ruby", 
                    "Docker", 
                    "Postgres", 
                    "React", 
                    "AWS"
                ]
            },
            {
                "companyName": "JCI",
                "jobRole": "Senior Software Engineer",
                "dateStart": "January 2021",
                "dateEnd": "January 2023",
                "description": "Responsible for maintaining and enhancing an established support portal application. This application consists of a Java backend and an Angular frontend, entirely hosted on AWS.",
                "technologies": [
                    "AWS",
                    "Java",
                    "Angular"
                ]
            },
            {
                "companyName": "3EN Cloud",
                "jobRole": "Senior Software Engineer",
                "dateStart": "January 2020",
                "dateEnd": "January 2021",
                "description": "Built end-to-end development of E-Commerce, 3PL, Shipping, Financial & bespoke integrations and apps, from scoping, requirements gathering and client engagement to architecting, development, and support. Led the transition and development of our in-house integration platform within AWS. Built bespoke integrations with NetSuite and third party systems. Developed customisations for clients' NetSuite systems. R&D of in-house frameworks, systems and applications.",
                "technologies": [
                    "AWS",
                    "NetSuite",
                    "React",
                    "Apache Camel",
                    "Java",
                    "Redux"
                ]
            }
        ]
    }

    Example 3:

    {
        "name": "Ryan Anderson",
        "jobRole": "Software Engineer II",
        "bio": "A Software Engineer with over 4 years full stack experience. He has experience developing PHP and Vue web applications. He also has had a focus on advanced testing and implementation, cluster optimisation and Java auditing for a major Tier 1 banking organisation.",
        "skills": "Java, C#, Typescript, Vue, PHP, JavaScript, CSS/SCSS, HTML, MSSQL, BASH, Python, Cypress",
        "experience": [
            {
                "companyName": "Galvia Digital",
                "jobRole": "Web Developer",
                "dateStart": "January 2023",
                "dateEnd": "January 2024",
                "description": "Developed two tailored component libraries in open-source leveraging technologies such as Vue.js, JavaScript, TypeScript and Laravel.",
                "technologies": [
                    "Vue.js", 
                    "JavaScript", 
                    "TypeScript", 
                    "Composition API", 
                    "Cypress", 
                    "Storybook", 
                    "PHP", 
                    "Laravel"
"
                ]
            },
            {
                "companyName": "Citigroup",
                "jobRole": "Java Developer",
                "dateStart": "January 2020",
                "dateEnd": "January 2023",
                "description": "Collaborated globally to optimise Java apps for analytics clusters, enhancing performance. Tested and implemented Trino Starburst query engine for seamless analytics integration. Improved cluster space utilisation by over 30% through codec introduction. Collaborated on Java auditing and pre-processing for efficient data transfer and UI output. Led a 12-week cross-sector project, delivering controlled access Java apps for external team's data requests. Initiated LightSpeed adoption POC, gaining expertise in Tekton, HELM, Docker, and OpenShift.",
                "technologies": [
                    "Java", 
                    "HADOOP DFS", 
                    "CyberArc", 
                    "CA AutoSys", 
                    "HELM", 
                    "Docker"
                ]
            }
        ]
    }

    This is the end of the examples.

    I am now going to provide some additional context which I want you to consider when generating the final CV.

    Additional Context:
    """ + additional_context + """

    Below, in single quotes, is the engineer's existing outdated CV. Use this as a reference for building the final CV after considering everything.
    """ + existing_cv + """

    Can you generate a CV considering all the provided information and context?
    """

    result = generator.run(prompt)
    print(result["replies"][0])
    # print(result)