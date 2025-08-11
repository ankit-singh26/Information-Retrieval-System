# 🧠 Information Retrieval System with Custom LLM Integration

A powerful full-stack application that enables users to upload PDF documents and retrieve context-aware answers using advanced AI models. The system integrates custom LLMs through OpenRouter API, supporting models like DeepSeek, Llama, and other cutting-edge language models.

## ✨ Key Features

- 📄 **PDF Document Processing**: Upload and intelligently parse PDF documents
- 🤖 **Custom LLM Integration**: Support for multiple LLMs via OpenRouter API (DeepSeek, Llama, Claude, etc.)
- 🔍 **Intelligent Q&A**: Ask questions and get accurate, context-aware answers from your documents
- 🧠 **Vector Search**: Advanced similarity search using FAISS for precise document retrieval
- 🛡️ **Secure Authentication**: JWT-based user authentication and authorization
- 🌐 **Modern Tech Stack**: FastAPI backend with React frontend
- 📊 **Real-time Processing**: Instant document analysis and question answering

## 🏗️ Project Architecture

```
information-retrieval-system/
├── client/                     # React Frontend Application
│   ├── public/                 # Static assets
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── Login.jsx       # User authentication
│   │   │   ├── Signup.jsx      # User registration
│   │   │   ├── Navbar.jsx      # Navigation component
│   │   │   ├── UploadAndAsk.jsx # Main Q&A interface
│   │   │   └── ChatHistory.jsx # Chat history display
│   │   ├── assets/             # Images and icons
│   │   ├── api.js              # Axios API configuration
│   │   ├── App.jsx             # Root component
│   │   └── main.jsx            # Application entry point
│   ├── index.html
│   ├── vite.config.js          # Vite configuration
│   ├── package.json
│   └── eslint.config.js
│
├── server/                     # FastAPI Backend
│   ├── faiss_index/           # FAISS vector database
│   ├── storage/               # Temporary file storage
│   ├── auth.py                # JWT authentication logic
│   ├── db.py                  # MongoDB connection setup
│   ├── model.py               # Pydantic data models
│   ├── main.py                # FastAPI application & routes
│   ├── utils.py               # Core AI/ML utilities
│   ├── job_skills.json        # Job skills reference data
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables
│
├── images/                    # Application screenshots
└── README.md
```

## 🚀 Advanced Features

### 🤖 Multi-LLM Support
- **OpenRouter Integration**: Access to 100+ AI models through a single API
- **Model Flexibility**: Switch between different LLMs (DeepSeek, Llama 3.1, Claude, GPT-4, etc.)
- **Cost Optimization**: Choose models based on performance and cost requirements
- **Fallback Support**: Automatic model switching for reliability

### 🧠 Intelligent Document Processing
- **Advanced Text Extraction**: PyMuPDF for high-quality PDF text extraction
- **Smart Chunking**: Recursive text splitting for optimal context preservation
- **Vector Embeddings**: Sentence-transformers for semantic understanding
- **Context-Aware Retrieval**: FAISS-powered similarity search

### 🔐 Enterprise-Grade Security
- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt encryption for user passwords
- **Protected Routes**: Role-based access control
- **CORS Configuration**: Secure cross-origin resource sharing

## 🛠️ Technology Stack

### Frontend
- **React 19.1.0**: Modern React with latest features
- **Vite**: Lightning-fast build tool and dev server
- **Tailwind CSS 4.1.11**: Utility-first CSS framework
- **Axios**: HTTP client for API communication
- **React Router DOM**: Client-side routing

### Backend
- **FastAPI**: High-performance Python web framework
- **LangChain**: Framework for LLM application development
- **OpenRouter API**: Access to multiple AI models
- **FAISS**: Facebook AI Similarity Search for vector operations
- **Motor**: Async MongoDB driver
- **PyMuPDF**: PDF processing and text extraction

### AI/ML Stack
- **Sentence Transformers**: Text embedding models
- **HuggingFace Transformers**: Pre-trained language models
- **OpenAI Compatible API**: Seamless integration with various LLMs
- **Vector Databases**: FAISS for similarity search

LangChain for chaining LLMs

Motor (MongoDB async driver)

Python-Jose + Passlib (Auth)

📦 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/ankit-singh26/Information-Retrieval-System.git
cd information-retrieval-gen-ai
2. Backend Setup
bash
Copy
Edit
cd server
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Environment Configuration
Create a `.env` file in the `server/` directory:

```env
# Database Configuration
MONGO_URI=mongodb://localhost:27017/genai_project
# For MongoDB Atlas: mongodb+srv://username:password@cluster.mongodb.net/genai_project

# Authentication
SECRET_KEY=your-super-secret-jwt-key-here
ALGORITHM=HS256

# OpenRouter API Configuration
OPENROUTER_API_KEY=your-openrouter-api-key-here
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct:free

# Optional: Custom model configurations
# OPENROUTER_MODEL=deepseek/deepseek-chat
# OPENROUTER_MODEL=anthropic/claude-3-haiku
# OPENROUTER_MODEL=openai/gpt-4o-mini
```

#### Start the Backend Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup

#### Navigate to Client Directory
```bash
cd ../client  # from server directory
# or
cd client     # from project root
```

#### Install Dependencies
```bash
npm install
```

#### Start Development Server
```bash
npm run dev
```

The application will be available at:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
## 🔧 Environment Variables Reference

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `MONGO_URI` | MongoDB connection string | `mongodb://localhost:27017/genai_project` |
| `SECRET_KEY` | JWT secret key for authentication | `your-super-secret-jwt-key-here` |
| `OPENROUTER_API_KEY` | OpenRouter API key for LLM access | `sk-or-v1-xxxxxxxxxxxxx` |

### Optional Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `OPENROUTER_MODEL` | LLM model to use | `meta-llama/llama-3.1-8b-instruct:free` |
| `ALGORITHM` | JWT algorithm | `HS256` |

### Supported LLM Models
The system supports various models through OpenRouter:

**Free Models:**
- `meta-llama/llama-3.1-8b-instruct:free`
- `microsoft/phi-3-medium-128k-instruct:free`
- `google/gemma-2-9b-it:free`

**Premium Models:**
- `deepseek/deepseek-chat` - DeepSeek's latest model
- `anthropic/claude-3-haiku` - Fast and efficient
- `openai/gpt-4o-mini` - OpenAI's efficient model
- `meta-llama/llama-3.1-70b-instruct` - Larger Llama model

## 🚀 Usage Guide

### 1. User Registration & Login
1. Navigate to the signup page
2. Create an account with email and password
3. Login to receive a JWT token
4. Token is automatically stored for subsequent requests

### 2. Document Upload & Processing
1. Upload a PDF document using the upload interface
2. The system automatically:
   - Extracts text from the PDF
   - Splits text into manageable chunks
   - Generates vector embeddings
   - Stores embeddings in FAISS index

### 3. Question & Answer
1. Ask questions about your uploaded document
2. The system:
   - Embeds your question
   - Retrieves relevant document chunks
   - Sends context to the selected LLM
   - Returns an intelligent answer

## 📚 How It Works

### Document Processing Pipeline
```mermaid
graph LR
    A[PDF Upload] --> B[Text Extraction]
    B --> C[Text Chunking]
    C --> D[Vector Embedding]
    D --> E[FAISS Storage]
```

### Question Answering Pipeline
```mermaid
graph LR
    A[User Question] --> B[Question Embedding]
    B --> C[Similarity Search]
    C --> D[Context Retrieval]
    D --> E[LLM Processing]
    E --> F[Generated Answer]
```

## 🧪 API Documentation

### Authentication Endpoints
| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/signup` | Register new user | `{"email": "user@example.com", "password": "password"}` |
| `POST` | `/login` | User authentication | `{"email": "user@example.com", "password": "password"}` |

### Document Processing Endpoints
| Method | Endpoint | Description | Headers | Request Body |
|--------|----------|-------------|---------|--------------|
| `POST` | `/upload` | Upload PDF document | `Authorization: Bearer <token>` | Form data with PDF file |
| `POST` | `/ask` | Ask question about document | `Authorization: Bearer <token>` | `{"query": "Your question here"}` |

### Utility Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/docs` | Interactive API documentation |

## 🔧 Configuration & Customization

### Model Selection
You can easily switch between different LLMs by updating the `OPENROUTER_MODEL` environment variable:

```bash
# For DeepSeek (recommended for coding tasks)
OPENROUTER_MODEL=deepseek/deepseek-chat

# For Claude (great for analysis)
OPENROUTER_MODEL=anthropic/claude-3-haiku

# For GPT-4 (premium option)
OPENROUTER_MODEL=openai/gpt-4o-mini
```

### Custom Prompt Templates
The system uses intelligent prompt templates that can be customized in `server/utils.py`:

```python
def build_prompt_template():
    prompt = """
You are an intelligent document analyzer...
    """
```

## 🚨 Troubleshooting

### Common Issues

**1. OpenRouter API Key Error**
```
ValueError: OPENROUTER_API_KEY not found in environment variables
```
**Solution**: Ensure your `.env` file contains a valid OpenRouter API key.

**2. MongoDB Connection Error**
```
ServerSelectionTimeoutError: No servers found
```
**Solution**: Check your MongoDB connection string and ensure the database is running.

**3. CORS Issues**
**Solution**: Ensure the frontend URL is properly configured in CORS settings.

**4. PDF Processing Errors**
**Solution**: Ensure uploaded files are valid PDF documents and not corrupted.

## 📤 Deployment

### Backend Deployment (Render/Railway)

1. **Create a new web service**
2. **Connect your GitHub repository**
3. **Set environment variables:**
   ```
   MONGO_URI=your-mongodb-atlas-connection-string
   SECRET_KEY=your-production-secret-key
   OPENROUTER_API_KEY=your-openrouter-api-key
   ```
4. **Build command:** `pip install -r requirements.txt`
5. **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend Deployment (Vercel/Netlify)

1. **Build settings:**
   - Build command: `npm run build`
   - Output directory: `dist`
2. **Update API base URL** in `client/src/api.js`
3. **Deploy from GitHub repository**

### Environment-Specific Configuration

**Production `.env`:**
```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/genai_project
SECRET_KEY=super-secure-production-key-minimum-32-characters
OPENROUTER_API_KEY=sk-or-v1-your-production-key
OPENROUTER_MODEL=deepseek/deepseek-chat
```

## 🖼️ Application Screenshots

### 1. User Authentication
![Login Page](images/images/login.png)
*Secure user authentication with JWT tokens*

![Signup Page](images/images/signup.png)
*User registration with email validation*

### 2. Document Processing & Q&A
![Upload Interface](images/images/upload.png)
*PDF upload and processing interface*

![Q&A Interface](images/images/image.png)
*Intelligent question-answering system*

## 🎯 Roadmap & Future Enhancements

- [ ] **Multi-document Support**: Handle multiple PDFs simultaneously
- [ ] **Chat History**: Persistent conversation history
- [ ] **File Type Expansion**: Support for DOCX, TXT, and other formats
- [ ] **Advanced Analytics**: Usage statistics and performance metrics
- [ ] **Team Collaboration**: Shared documents and workspaces
- [ ] **API Rate Limiting**: Enhanced security and usage controls
- [ ] **Caching Layer**: Redis integration for improved performance
- [ ] **Mobile App**: React Native mobile application

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit changes:** `git commit -m 'Add amazing feature'`
4. **Push to branch:** `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint configuration for JavaScript/React
- Write comprehensive tests for new features
- Update documentation for API changes

## 📊 Performance & Scalability

- **Vector Search**: FAISS provides sub-second similarity search
- **Async Operations**: FastAPI and Motor for high concurrency
- **Caching**: In-memory vector storage for fast retrieval
- **Scalability**: Horizontal scaling support with load balancers

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt with salt for password security
- **Input Validation**: Pydantic models for request validation
- **CORS Protection**: Configurable cross-origin resource sharing
- **File Upload Security**: PDF validation and size limits

## 🙏 Acknowledgments

- **OpenRouter** for providing access to multiple LLM APIs
- **LangChain** for the excellent framework for LLM applications
- **FAISS** by Facebook AI for efficient similarity search
- **FastAPI** for the high-performance web framework
- **React** and **Vite** for the modern frontend development experience

---

**Made with ❤️ by the development team**

For support or questions, please open an issue on GitHub or contact the maintainers.

