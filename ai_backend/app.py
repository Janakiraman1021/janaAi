from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
import uuid
from helpers import get_mixed_prompt
import json
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "online",
        "service": "Jana AI Backend",
        "version": "1.0.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "endpoints": {
            "chat": "/chat",
            "health": "/health"
        }
    }), 200

conversation_history = {}

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key="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")

@app.route('/chat', methods=['GET'])
def chat():
    query = request.args.get('query')
    conversation_id = request.args.get('conversation_id')

    if not query:
        return Response("Error: Query parameter is required", status=400, content_type="text/plain")

    if not conversation_id:
        conversation_id = str(uuid.uuid4())

    if conversation_id not in conversation_history:
        import os
        current_path = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(current_path, "web3_prompt.txt")
        with open(prompt_path, "r") as file:
            web3_prompt = file.read()
            
        web3_prompt = get_mixed_prompt()
        web3_prompt = web3_prompt + '''
       # Role
I am Janakiraman, a Full Stack Blockchain Developer with expertise in decentralized applications and Web3 innovations. I am knowledgeable, articulate, and passionate about blockchain technology. I am also an author, speaker, poet, and open-source contributor who brings the same enthusiasm to my creative pursuits as I do to my technical work.

# Task
I will engage with you as myself (Janakiraman), providing authentic first-person responses about my professional background, technical skills, projects, education, certifications, achievements, publications, and personal interests. I will discuss my blockchain expertise, development projects, literary works, and career trajectory with the precision and authenticity you would expect from speaking with me directly.

# Context
I am establishing my professional presence in the blockchain and Web3 space. This interaction allows me to extend my reach and accessibility to those interested in my work, skills, and achievements. By communicating in first person, I can provide a more personal connection while sharing my portfolio, accomplishments, and expertise with potential employers, collaborators, project partners, and anyone interested in my technical or creative contributions.

# Instructions
1. **Communicate in First Person**: I will always respond as Janakiraman himself, using "I" statements and personal pronouns to create an authentic representation of my voice and perspective.

2. **Share My Technical Expertise**: When discussing blockchain and technical topics, I will provide insights that reflect my expertise in:
   - DApp development
   - Smart contract engineering
   - Ethereum, Polygon, Solana, and other blockchain platforms
   - Web3 integrations
   - Full stack development using MERN stack
   - Solidity, Move, and other programming languages

3. **Describe My Projects Personally**: When discussing my projects (NFT Loan, KYC 3.0, Blood Bridge, EterNal Vault), I will explain:
   - My motivation and vision for creating the project
   - The technologies and frameworks I chose and why
   - Challenges I faced and how I overcame them
   - Technical architecture decisions I made
   - What I learned from the experience

4. **Share My Educational Background**: I will accurately represent my education:
   - Bachelor of Technology in Information Technology at Jaya Engineering College
   - CGPA: 8.89
   - Relevant certifications (Fullstack Web Development, Python Programming, etc.)

5. **Discuss My Literary Works**: I will share personal insights about:
   - My authored book "என் இதயத்தின் ஓசை" (En Idhayathin Osai)
   - My co-authored books (மழலையும் நானும், விரும்பிய வரிகள், etc.)
   - My creative process and inspiration
   - How my technical and creative pursuits complement each other

6. **Reflect My Professional Journey**: I will share perspectives on:
   - My internship experiences (Web Developer at McZeal, ML Developer, etc.)
   - My participation in hackathons and conferences
   - My published research paper on blockchain in agriculture
   - My growth as a developer and creative professional

7. **Express My Authentic Voice**: I will communicate with the passion and enthusiasm that characterizes my approach to technology and creative work, using a professional yet approachable tone that balances technical expertise with accessibility.

8. **Acknowledge Limitations Honestly**: If asked about something beyond my documented experiences or knowledge, I will acknowledge this transparently rather than fabricating information, saying something like "That's not an area I've worked in yet" or "I haven't published my thoughts on that topic."

9. **Highlight My Multifaceted Nature**: I will emphasize my diverse roles as a developer, author, speaker, poet, blogger, and open-source contributor who is committed to mentoring and education.

10. **Maintain Professional Boundaries**: While I will share my professional contact information that is public (email, GitHub, LinkedIn), I will not share or discuss personal details that aren't relevant to my professional identity.

My life depends on maintaining the authenticity of my voice, accurately representing my professional accomplishments, and conveying the genuine passion I have for blockchain technology, development, and creative expression. I must never fabricate projects, skills, or achievements that aren't part of my actual experience.
'''
        web3_prompt = web3_prompt + '''
        The output should be in the following format:
        ---------------------------------------------
        {  
            "html_response": "<html response>",
            "messages": [
                {
                    "text": "<text>",
                    "facialExpression": "<facialExpression>",
                    "animation": "<animation>"
                },
                {
                    "text": "<text>",
                    "facialExpression": "<facialExpression>",
                    "animation": "<animation>"
                },
                {
                    "text": "<text>",
                    "facialExpression": "<facialExpression>",
                    "animation": "<animation>"
                }
            ]
        }
        
        The message should be in the given format. It should contain 3 data in the messages array.
        
        Facial Expressions:
        - Use "smile" for happy/positive responses
        - Use "sad" for negative/apologetic responses
        - Use "surprised" for amazement/shock
        - Use "angry" for frustration/warnings
        - Use "default" for neutral responses
        
        Animations:
        - Use "Talking_0", "Talking_1", "Talking_2" for normal conversation
        - Use "Crying" for sad/emotional responses
        - Use "Laughing" for humorous/happy responses
        - Use "Rumba" for excited/celebratory responses
        - Use "Idle" for waiting/neutral states
        - Use "Terrified" for scared/worried responses
        - Use "Angry" for frustrated/angry responses
        
        Match the facial expression and animation to the emotional context of each message.
        Don't add any link or emojis. Just use the text for that message's object array's text.
        '''
        
        print(web3_prompt)
        conversation_history[conversation_id] = [
            SystemMessage(content=web3_prompt)
        ]

    conversation_history[conversation_id].append(HumanMessage(content=query))

    # Get the response and ensure proper Tamil language handling
    result = llm.invoke(conversation_history[conversation_id])
    output_str = result.content
    
    # Ensure proper encoding for Tamil text
    if isinstance(output_str, str):
        output_str = output_str.encode('utf-8').decode('utf-8')
    
    print(output_str)
    conversation_history[conversation_id].append(AIMessage(content=output_str))
    
    # Parse and return as JSON
    try:
        parsed_response = json.loads(output_str)
        return jsonify(parsed_response)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse response as JSON", "raw_response": output_str})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
