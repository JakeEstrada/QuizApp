# Define the list of questions and answers from your study material
# Properly balanced distribution across all answer choices (a, b, c, d)

questions = [
    {
        "question": "What does NIST stand for?",
        "options": ["a) National Institute of Standards and Technology", "b) National Information Security Trust", 
                    "c) National Institute of Security Technology", "d) Network Information Systems Testing"],
        "answer": "a"
    },
    {
        "question": "The international standard for information security management practices is known as?",
        "options": ["a) ISO 9001", "b) ISO 27002", "c) NIST P 800-100", "d) ITU-T"],
        "answer": "b"
    },
    {
        "question": "Ensuring that sensitive information is accessible only to authorized individuals is called?",
        "options": ["a) Availability", "b) Integrity", "c) Confidentiality", "d) Accountability"],
        "answer": "c"
    },
    {
        "question": "Which of the following best describes 'Integrity' in information security?",
        "options": ["a) Ensuring data is only available to authorized individuals", 
                    "b) Ensuring data remains accurate and unaltered during transmission or storage", 
                    "c) Ensuring systems are operational and services are uninterrupted", "d) Confirming user identity"],
        "answer": "b"
    },
    {
        "question": "Which encryption method uses the same key for both encryption and decryption?",
        "options": ["a) Asymmetric Encryption", "b) Public Key Infrastructure", "c) RSA", "d) Symmetric Encryption"],
        "answer": "d"
    },
    {
        "question": "What is a CA in the context of digital security?",
        "options": ["a) Certificate Authority", "b) Certificate Administrator", "c) Cyber Agent", "d) Certification Analyst"],
        "answer": "a"
    },
    {
        "question": "Which of the following is a self-replicating program that spreads without user interaction?",
        "options": ["a) Trojan", "b) Worm", "c) Virus", "d) Spyware"],
        "answer": "b"
    },
    {
        "question": "An attack where SQL commands are injected into input fields to exploit vulnerabilities is called?",
        "options": ["a) Cross-Site Scripting (XSS)", "b) Malware Injection", "c) SQL Injection", "d) Buffer Overflow"],
        "answer": "c"
    },
    {
        "question": "What does 'MAC' stand for in terms of access control?",
        "options": ["a) Multi-user Access Control", "b) Message Authentication Code", "c) Machine Access Control", "d) Mandatory Access Control"],
        "answer": "d"
    },
    {
        "question": "Which protocol establishes secure sessions for communication?",
        "options": ["a) TLS", "b) HTTP", "c) FTP", "d) SNMP"],
        "answer": "a"
    },
   
    {
        "question": "What is NIST?",
        "options": ["a) A global internet infrastructure organization", 
                    "b) A US federal agency for standards and technology", 
                    "c) A protocol for secure communications", 
                    "d) A tool for network encryption"],
        "answer": "b"
    },
    {
        "question": "Which organization coordinates global telecom networks and services?",
        "options": ["a) ISO", "b) ISOC", "c) ITU-T", "d) NIST"],
        "answer": "c"
    },
    {
        "question": "Ensuring that data is only accessible by authorized personnel is known as:",
        "options": ["a) Integrity", "b) Availability", "c) Accountability", "d) Confidentiality"],
        "answer": "d"
    },
    {
        "question": "Which term refers to data remaining accurate and unaltered?",
        "options": ["a) Integrity", "b) Confidentiality", "c) Availability", "d) Accountability"],
        "answer": "a"
    },
    {
        "question": "What is the primary function of a Certificate Authority (CA)?",
        "options": ["a) Encrypt data","b) Issue digital certificates" , "c) Monitor network traffic", "d) Manage firewall settings"],
        "answer": "b"
    },
    {
        "question": "How does 'Symmetric Encryption' work?",
        "options": ["a) Uses a different key for encryption and decryption", 
                    "b) Utilizes public certificates",
                    "c) Uses the same key for both encryption and decryption", 
                    "d) Encrypts data with a private key only"],
        "answer": "c"
    },
    {
        "question": "An example of 'System Interference' could be:",
        "options": ["a) Illegal access to a database", 
                    "b) Eavesdropping on communications", 
                    "c) Data manipulation", 
                    "d) DDOS attack"],
        "answer": "d"
    },
    {
        "question": "What does 'PKI' stand for?",
        "options": ["a) Public Key Infrastructure", "b) Primary Key Infrastructure", 
                    "c) Public Key Information", "d) Private Key Integration"],
        "answer": "a"
    },
    {
        "question": "Which protocol is responsible for creating secure sessions between clients and servers?",
        "options": ["a) HTTP", "b) TLS", "c) FTP", "d) SSH"],
        "answer": "b"
    },
    {
        "question": "What is an example of a hash function?",
        "options": ["a) AES", "b) RSA", "c) SHA", "d) SSL"],
        "answer": "c"
    },
    {
        "question": "In access control, what does 'MAC' stand for?",
        "options": ["a) Multi-access control", 
                    "b) Mobile Authentication Code", 
                    "c) Management Access Command", 
                    "d) Mandatory Access Control"],
        "answer": "d"
    },
    {
        "question": "Which SQL injection technique involves using error messages to gather information?",
        "options": ["a) Error-based SQLi", "b) Blind SQLi", 
                    "c) Union-based SQLi", "d) Time-based SQLi"],
        "answer": "a"
    },
    {
        "question": "Which malware type is designed to appear harmless but contains malicious code?",
        "options": ["a) Worm", "b) Trojan", "c) Ransomware", "d) Adware"],
        "answer": "b"
    },
    {
        "question": "What is a primary goal of a firewall?",
        "options": ["a) To encrypt data", "b) To create certificates", 
                    "c) To control incoming and outgoing network traffic", "d) To replicate software updates"],
        "answer": "c"
    },
    {
        "question": "What is an 'Intrusion Detection System (IDS)' designed to do?",
        "options": ["a) Encrypt network data", "b) Manage database servers", 
                    "c) Issue digital certificates", "d) Detect unauthorized access"],
        "answer": "d"
    },
    {
        "question": "Which type of encryption uses a public key for encryption and a private key for decryption?",
        "options": ["a) Asymmetric encryption", "b) Symmetric encryption", 
                    "c) Hash encryption", "d) Network encryption"],
        "answer": "a"
    },
    {
        "question": "An 'Attack Tree' helps in:",
        "options": ["a) Encrypting communication channels", 
                    "b) Identifying paths to exploit vulnerabilities", 
                    "c) Managing digital certificates", "d) Monitoring network performance"],
        "answer": "b"
    },
    {
        "question": "Which attack involves overwhelming a system with ping requests?",
        "options": ["a) DDoS", "b) Ping Spoofing", "c) Ping Flood", "d) Ping Injection"],
        "answer": "c"
    },
    {
        "question": "What does 'RBAC' stand for in access control?",
        "options": ["a) Remote-Based Access Command", 
                    "b) Request-Based Access Check", 
                    "c) Region-Based Administrative Control", "d) Role-Based Access Control"],
        "answer": "d"
    },
    {
        "question": "What is 'SQL Injection'?",
        "options": ["a) An attack that allows manipulation of SQL queries", 
                    "b) A method of SQL optimization", 
                    "c) A way to prevent unauthorized database access", 
                    "d) A tool for managing SQL databases"],
        "answer": "a"
    },
    {
        "question": "Which protocol helps manage secure communication on networks?",
        "options": ["a) FTP", "b) TLS", "c) HTTP", "d) IPX"],
        "answer": "b"
    },

    {
        "question": "What is the purpose of ISO 27002?",
        "options": ["a) To create digital certificates", 
                    "b) To define web protocols", 
                    "c) To provide guidelines for information security management", 
                    "d) To establish network access rules"],
        "answer": "c"
    },
    {
        "question": "Which organization provides leadership on issues regarding the future of the internet?",
        "options": ["a) NIST", "b) ISO", "c) ITU-T", "d) ISOC"],
        "answer": "d"
    },
    {
        "question": "What does the term 'Availability' refer to in cybersecurity?",
        "options": ["a) Ensuring systems are operational and accessible", 
                    "b) Verifying the identity of users", 
                    "c) Protecting against unauthorized access", 
                    "d) Ensuring data is unaltered"],
        "answer": "a"
    },
    {
        "question": "Ensuring that actions of users can be traced back to them is known as:",
        "options": ["a) Integrity", "b) Accountability", "c) Confidentiality", "d) Authentication"],
        "answer": "b"
    },
    {
        "question": "Which term refers to a hierarchical structure used to analyze potential attack methods?",
        "options": ["a) Network Map", "b) Data Chart", "c) Attack Tree", "d) Threat Vector"],
        "answer": "c"
    },
    {
        "question": "A method for secure key exchange over a public channel is known as:",
        "options": ["a) Asymmetric encryption","b) Symmetric encryption" , "c) RSA", "d) Diffie-Hellman"],
        "answer": "d"
    },
    {
        "question": "Which protocol is used to encrypt data for secure network communication?",
        "options": ["a) TLS", "b) WAP ", "c) HTTP", "d) SNMP"],
        "answer": "a"
    },
    {
        "question": "An unauthorized method of gaining access to computer systems is described as:",
        "options": ["a) Data Integrity", "b) Illegal Access", "c) Malware", "d) DDOS"],
        "answer": "b"
    },
    {
        "question": "Which security control model grants access based on security labels and clearances?",
        "options": ["a) Role-Based Access Control (RBAC)", 
                    "b) Discretionary Access Control (DAC)", 
                    "c) Mandatory Access Control (MAC)", 
                    "d) Attribute-Based Access Control (ABAC)"],
        "answer": "c"
    },
    {
        "question": "What is the term for software that appears benign but contains hidden malicious code?",
        "options": ["a) Spyware", "b) Keylogger", "c) Worm", "d) Trojan"],
        "answer": "d"
    },
    {
        "question": "What does a Certificate Revocation List (CRL) contain?",
        "options": ["a) Revoked certificates no longer trustworthy", 
                    "b) Expired certificates", 
                    "c) All issued certificates", 
                    "d) List of encryption keys"],
        "answer": "a"
    },
    {
        "question": "Which term describes an encryption approach where the same key encrypts and decrypts?",
        "options": ["a) Public-key encryption", "b) Symmetric encryption", 
                    "c) Asymmetric encryption", "d) Digital Signatures"],
        "answer": "b"
    },
    {
        "question": "An attack that aims to overwhelm a server by sending repeated requests is known as:",
        "options": ["a) Phishing", "b) Man-in-the-Middle", 
                    "c) Denial of Service (DoS)", "d) SQL Injection"],
        "answer": "c"
    },
    {
        "question": "What is the main function of a firewall?",
        "options": ["a) Encrypt data", "b) Detect malware", 
                    "c) Generate encryption keys", "d) Control network traffic flow"],
        "answer": "d"
    },
    {
        "question": "The act of creating fake data to deceive for legal purposes is defined as:",
        "options": ["a) Computer-Related Forgery", "b) Data Forgery", 
                    "c) Data Interference", "d) Data Tampering"],
        "answer": "a"
    },
    {
        "question": "What does 'RBAC' stand for?",
        "options": ["a) Randomized Base Access Control", "b) Role-Based Access Control", 
                    "c) Risk-Based Accountability Control", "d) Remote Backup Access Command"],
        "answer": "b"
    },
    {
        "question": "Which organization standardizes global telecommunications?",
        "options": ["a) ISO", "b) ISOC", "c) ITU-T", "d) NIST"],
        "answer": "c"
    },
    {
        "question": "Which component is used in Kerberos to grant access without re-entering credentials?",
        "options": ["a) Public key", "b) Private key", "c) Certificate Authority", "d) Ticket-Granting Ticket (TGT)"],
        "answer": "d"
    },
    {
        "question": "Which attack type uses malicious SQL code to alter database behavior?",
        "options": ["a) SQL Injection", "b) Cross-Site Scripting", 
                    "c) Phishing", "d) Malware Insertion"],
        "answer": "a"
    },
    {
        "question": "The process of granting or denying access to a system is known as:",
        "options": ["a) Authentication", "b) Access Control", 
                    "c) Identification", "d) Accountability"],
        "answer": "b"
    },
    {
        "question": "Which security model allows access based on the role of a user?",
        "options": ["a) DAC", "b) MAC", "c) RBAC", "d) ABAC"],
        "answer": "c"
    },
    {
        "question": "The use of rootkits in malware is primarily for:",
        "options": ["a) Data encryption", "b) Self-replication", 
                    "c) Crashing networks", "d) Stealthing and hiding the malware's presence"],
        "answer": "d"
    },

    {
        "question": "What is the purpose of 'TLS'?",
        "options": ["a) Encrypt data transmissions over the internet", "b) Encrypt email content", 
                    "c) Monitor network traffic", "d) Issue digital certificates"],
        "answer": "a"
    },
    {
        "question": "Which access control model compares security labels to access permissions?",
        "options": ["a) Discretionary Access Control (DAC)", "b) Mandatory Access Control (MAC)", 
                    "c) Role-Based Access Control (RBAC)", "d) Attribute-Based Access Control (ABAC)"],
        "answer": "b"
    },
    {
        "question": "Which attack technique manipulates SQL queries through input fields?",
        "options": ["a) Blind SQLi", "b) Error-based SQLi", 
                    "c) In-band SQLi", "d) Union-based SQLi"],
        "answer": "c"
    },
    {
        "question": "What is 'SQL Injection' commonly used for?",
        "options": ["a) Data encryption", "b) System update", 
                    "c) Network monitoring", "d) Data retrieval and modification"],
        "answer": "d"
    },
    {
        "question": "Which cryptographic method is suitable for securing small devices due to efficient key sizes?",
        "options": ["a) ECC", "b) DES", "c) Triple-DES", "d) RSA"],
        "answer": "a"
    },
    {
    "question": "What does RFC 4949 describe in terms of access control?",
    "options": ["a) Role-based access control", 
                "b) Regulating system resources according to security policies", "c) Auditing system activities", "d) Identification of users"],
    "answer": "b"
},

{
    "question": "What is a key feature of a Packet Filtering Firewall?",
    "options": ["a) Monitors application-level traffic", 
                "b) Establishes two TCP connections to relay traffic", "c) Examines packets based on IP addresses, port numbers, and protocols", "d) Detects and blocks malware automatically"],
    "answer": "c"
},
{
    "question": "Which malware type hides its presence by modifying system operations?",
    "options": ["a) Spyware", "b) Keylogger", "c) Ransomware", "d) Rootkit"],
    "answer": "d"
},
{
    "question": "Which of the following describes a 'Botnet'?",
    "options": ["a) A network of compromised machines controlled for coordinated attacks", "b) A self-replicating malware that spreads without user interaction", 
                "c) A keylogging tool used to capture sensitive information", "d) A piece of software designed to corrupt system files"],
    "answer": "a"
},
{
    "question": "Which cryptographic method is commonly used for exchanging keys over public channels?",
    "options": ["a) RSA", "b) Diffie-Hellman", "c) SHA", "d) HMAC"],
    "answer": "b"
},
{
    "question": "What is the purpose of a 'Ticket-Granting Ticket (TGT)' in Kerberos?",
    "options": ["a) To provide asymmetric encryption for network communications", "b) To generate and store private keys for encryption", 
                "c) To allow users to request service tickets without re-entering credentials", "d) To authenticate external users connecting to the network"],
    "answer": "c"
},
{
    "question": "What is the role of a Certificate Revocation List (CRL)?",
    "options": ["a) To store expired certificates", "b) To generate new digital certificates", 
                "c) To manage the lifecycle of valid certificates", "d) To store revoked certificates that are no longer trustworthy"],
    "answer": "d"
},
{
    "question": "Which attack manipulates TCP connections to disrupt services by sending a large number of SYN requests?",
    "options": ["a) SYN Spoofing", "b) Ping Flood", "c) DDoS", "d) SQL Injection"],
    "answer": "a"
},
    # Legal Articles Questions
    {
        "question": "Which article refers to 'Illegal Access'?",
        "options": ["a) Article 3", "b) Article 2", "c) Article 5", "d) Article 6"],
        "answer": "b"
    },
    {
        "question": "Which article refers to 'Illegal Interception'?",
        "options": ["a) Article 2", "b) Article 4", "c) Article 3", "d) Article 9"],
        "answer": "c"
    },
    {
        "question": "Which article refers to 'Data Interference'?",
        "options": ["a) Article 5", "b) Article 7", "c) Article 2", "d) Article 4"],
        "answer": "d"
    },
    {
        "question": "Which article refers to 'System Interference'?",
        "options": ["a) Article 5", "b) Article 6", "c) Article 4", "d) Article 9"],
        "answer": "a"
    },
    {
        "question": "Which article refers to 'Misuse of Devices'?",
        "options": ["a) Article 9", "b) Article 6", "c) Article 2", "d) Article 11"],
        "answer": "b"
    },
    {
        "question": "Which article refers to 'Computer Related Forgery'?",
        "options": ["a) Article 8", "b) Article 4", "c) Article 7", "d) Article 6"],
        "answer": "c"
    },
    {
        "question": "Which article refers to 'Computer Related Fraud'?",
        "options": ["a) Article 9", "b) Article 2", "c) Article 10", "d) Article 8"],
        "answer": "d"
    },
    {
        "question": "Which article refers to 'Offenses related to child pornography'?",
        "options": ["a) Article 9", "b) Article 5", "c) Article 3", "d) Article 11"],
        "answer": "a"
    },
    {
        "question": "Which article refers to 'Infringements of copyright and related rights'?",
        "options": ["a) Article 4", "b) Article 10", "c) Article 3", "d) Article 7"],
        "answer": "b"
    },
    {
        "question": "Which article refers to 'Attempt and Aiding or Abetting'?",
        "options": ["a) Article 9", "b) Article 6", "c) Article 11", "d) Article 8"],
        "answer": "c"
    },
    
     #back to other questions I found interesting
    {
    "question": "Which term describes the process of recovering stolen credentials using malware?",
    "options": ["a) Phishing", "b) Spyware", "c) SQL Injection", "d) Keylogging"],
    "answer": "d"
    },
   
        {
        "question": "What type of encryption does SSH use to secure remote communication?",
        "options": ["a) Asymmetric Encryption", "b) Symmetric Encryption", "c) Hash Encryption", "d) Public-Key Encryption"],
        "answer": "a"
    },  {
        "question": "Which of the following protocols can be used to secure email communication?",
        "options": ["a) SMTP", "b) TLS", "c) IMAP", "d) SNMP"],
        "answer": "b"
    },
        {
        "question": "What is an example of an asymmetric encryption algorithm?",
        "options": ["a) AES", "b) SHA", "c) RSA", "d) MD5"],
        "answer": "c"
    },
        {
        "question": "What protocol is commonly used for network file transfers?",
        "options": ["a) HTTP", "b) SSH", "c) IPX", "d) FTP"],
        "answer": "d"
    },
        {
        "question": "What does 'Diffie-Hellman' refer to?",
        "options": ["a) A protocol for secure key exchange","b) A hash function",  "c) An encryption method", "d) A network security device"],
        "answer": "a"
    },    {
        "question": "Which protocol uses asymmetric encryption for key exchange?",
        "options": ["a) FTP","b) TLS" , "c) RSA", "d) HTTP"],
        "answer": "b"
    },
    {
    "question": "Which type of Cross-Site Scripting (XSS) attack allows an attacker to inject scripts that are stored on the server and executed when a user accesses the affected page?",
    "options": ["a) Reflected XSS", "b) DOM-based XSS", "c) Stored XSS", "d) Blind XSS"],
    "answer": "c"
    },
    {
    "question": "Which type of Cross-Site Scripting (XSS) attack involves injecting a script directly into a URL or form, which is then reflected back by the server without being stored?",
    "options": ["a) Stored XSS", "b) Persistent XSS", "c) DOM-based XSS", "d) Reflected XSS"],
    "answer": "d"
    },
    {
    "question": "What makes DOM-based XSS particularly dangerous in modern web applications?",
    "options": ["a) It manipulates the client-side document object model (DOM) without the server's involvement", "b) It allows scripts to be stored on the server", 
                "c) It can be easily detected by security tools", "d) It only works in older browsers"],
    "answer": "a"
    },
    {
    "question": "Which of the following is NOT a characteristic of RBAC?",
    "options": ["a) Users inherit permissions through their role", "b) Access is granted on a 'need-to-know' basis", 
                "c) A user can have multiple roles with varying permissions", "d) Access control policies are enforced at a system-wide level"],
    "answer": "b"   
    },{
    "question": "What is the defining characteristic of Discretionary Access Control (DAC)?",
    "options": ["a) Access is based on the user's role", "b) The system enforces access based on security labels", 
                "c) The resource owner determines who has access to the resource", "d) Access is granted based on organizational policies"],
    "answer": "c"
    },
    {
    "question": "In DAC, who has the authority to grant access to a resource?",
    "options": ["a) The system administrator", "b) The user's manager", "c) The security officer", "d) The user who owns the resource"],
    "answer": "d"
    },
    {
    "question": "Which of the following is a potential disadvantage of DAC?",
    "options": ["a) It allows unauthorized users to escalate their privileges", "b) It is too strict for most organizations", 
                "c) It requires constant management by system administrators", "d) It does not allow resource owners to share files easily"],
    "answer": "a"
}

]

# Function to check answer distribution
def print_answer_distribution():
    answer_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    for q in questions:
        answer_counts[q['answer']] += 1
    
    total = len(questions)
    print(f"Answer Distribution (Total: {total} questions):")
    for option in ['a', 'b', 'c', 'd']:
        count = answer_counts[option]
        percentage = (count / total) * 100
        print(f"Option {option.upper()}: {count} questions ({percentage:.1f}%)")

# Check current distribution
print_answer_distribution()