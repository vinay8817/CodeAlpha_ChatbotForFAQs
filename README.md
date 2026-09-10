# FAQSphere AI 🌐🤖
### One Intelligent FAQ Assistant for Every Domain

> **CodeAlpha Artificial Intelligence Internship — Task 2**  
> Built by: Artificial Intelligence Intern  
> Production-Quality Multi-Domain NLP FAQ Web Application

---

## 🌟 Executive Summary

**FAQSphere AI** is a universal, multi-domain AI FAQ platform designed to eliminate rigid, single-company chatbot restrictions. Built with a modern dark/light SaaS aesthetic, it hosts a knowledge base of **22+ domains** and **220+ curated real-world FAQs**.

The application operates an in-browser Natural Language Processing (NLP) matching engine based on **TF-IDF Vectorization**, **Porter Stemming**, and **Cosine Similarity Scoring**. It allows users to query in everyday natural language without requiring exact keyword matches, respects domain-aware scoping, provides explainable confidence metrics, offers relevant related questions, and delivers graceful smart fallbacks when questions are outside the knowledge base.

---

## ✨ Key Features & Capabilities

- **22+ Diverse Domains**: Technology, Programming, Artificial Intelligence, Machine Learning, Web Development, Mobile Development, Cybersecurity, Cloud Computing, Software & SaaS, E-Commerce, Banking & Finance, Healthcare & Wellness, Travel & Hospitality, Food & Restaurants, Government Services, Jobs & Careers, Human Resources, Business & Startups, Real Estate, Education & University, Legal & Compliance, Productivity & Habits, Data Science & Big Data, DevOps & CI/CD, Entertainment & Gaming, Marketing & SEO, and Environment & Climate.
- **220+ Curated FAQs**: Realistic, high-quality questions and detailed technical answers equipped with domain tags, category labels, and search keywords.
- **In-Browser NLP Matching Engine**:
  - Punctuation stripping & lowercasing normalization
  - English stopword removal (with conversational filler filtering)
  - Morphological Porter Stemmer algorithm (e.g., `"computing"` $\to$ `"comput"`)
  - N-gram feature generation (unigrams + bigrams for phrases like `"cloud_comput"`)
  - Smooth Inverse Document Frequency ($\text{IDF}$) weighting
  - Vector Space Cosine Similarity calculation
  - Keyword tag boosting & exact substring enhancement
- **Domain-Aware & Global Scoping**:
  - Search within a designated domain (e.g., Programming)
  - Switch anytime to "All Domains" for universal search
  - Cross-domain fallback alerts (e.g. if asking about cloud computing in Technology, suggests matching Cloud Computing FAQ)
- **Smart Fallback Mechanism ("Did You Mean?")**:
  - Never invents or hallucinates answers when confidence is below threshold
  - Displays top 3 partial matches or domain recommendations
  - Provides quick action buttons to search all domains or browse FAQs
- **Interactive Modern Chatbot Interface**:
  - Bot and user avatars, responsive message bubbles, timestamps
  - Animated typing indicator with realistic simulated thinking delay
  - Confidence scoring badge (`High Match (88%)` / `Good Match (64%)`)
  - Expandable **"NLP Details"** breakdown showing similarity score and matched tokens
  - **3–5 Dynamic Related Questions** underneath each answer (one-click to answer)
  - One-click copy answer to clipboard with toast notification
  - Persistent chat history saved locally in `localStorage`
  - Clear conversation button with instant reset
- **Interactive FAQ Explorer**:
  - Live search across questions, answers, and tags
  - Dynamic category pill tabs
  - Expandable accordion answers with smooth animations
  - Direct "Ask this in Chatbot" button
  - Copy Answer and Share capabilities
- **Global Search Modal (`Ctrl+K` / `Cmd+K`)**:
  - Instant modal accessible from anywhere on the site
  - Live results grouped by domain with category tags
- **Theme Switcher**:
  - Seamless Light and Dark modes with `localStorage` preference memory
  - High-contrast typography and subtle glowing gradient SaaS styling
- **100% Privacy & Zero API Cost**:
  - Runs completely client-side in the browser
  - No remote tracking, no OpenAI keys, no paid subscription dependencies

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend Framework** | React 19, TypeScript |
| **Build Tool & Dev Server** | Vite 6 |
| **Styling & Theme** | Tailwind CSS v4, Custom Glassmorphism, CSS Animations |
| **Iconography** | Lucide React |
| **NLP Engine** | Custom In-Browser TypeScript TF-IDF + Cosine Similarity Vectorizer |
| **Python Counterpart** | `nlp_matching_demo.py` (standalone pure-Python vector math script) |
| **Storage & State** | React Context API, `localStorage` persistence |

---

## 📂 Project Architecture

```
d:/Chatbot/
├── index.html                  # HTML entry with Plus Jakarta Sans & meta tags
├── package.json                # Project dependencies & npm scripts
├── vite.config.ts              # Vite 6 config with Tailwind CSS v4 plugin
├── tsconfig.json               # TypeScript base config
├── tsconfig.app.json           # Application TypeScript compiler options
├── tsconfig.node.json          # Node/tooling TypeScript compiler options
├── nlp_matching_demo.py        # Standalone Python NLP demonstration script
├── README.md                   # Comprehensive project documentation
└── src/
    ├── main.tsx                # React DOM root mounting
    ├── App.tsx                 # Root component with routing and modals
    ├── index.css               # Tailwind CSS v4 styles, glassmorphism, animations
    ├── types/
    │   └── index.ts            # TypeScript interfaces (Domain, FAQ, ChatMessage, MatchResult)
    ├── data/
    │   └── faqData.ts          # 22+ domains and 220+ verified FAQs
    ├── nlp/
    │   └── nlpEngine.ts        # Porter Stemmer, Tokenizer, TF-IDF Vectorizer, Cosine Similarity
    ├── context/
    │   └── AppContext.tsx      # Global state (Theme, ActiveTab, Domain, Chat, Toast, Search)
    ├── components/
    │   ├── Navbar.tsx          # Responsive navigation, search trigger, theme toggle, mobile drawer
    │   ├── Footer.tsx          # Brand links, internship attribution, stats
    │   ├── DynamicIcon.tsx     # Dynamic Lucide icon mapper for domain cards
    │   ├── GlobalSearchModal.tsx # Ctrl+K global search popup
    │   └── Toast.tsx           # Floating notification toast
    └── pages/
        ├── HomePage.tsx        # Hero with glowing orb, quick-ask bar, metrics, popular domains, pipeline
        ├── DomainsPage.tsx     # Full domain directory with search, filter groups, and A-Z sorting
        ├── FaqExplorerPage.tsx # Domain switcher, category filters, expandable accordion, copy/share
        ├── ChatbotPage.tsx     # Full chatbot, domain selector, NLP confidence badges, related chips
        └── AboutPage.tsx       # System architecture, mathematical formulas, extensibility guide
```

---

## 🚀 Quick Start Guide

### Option 1: Open Directly by Double-Clicking `index.html`
You can open and run the entire application directly as a standalone HTML file:
1. Open your `d:/Chatbot/` folder in Windows File Explorer.
2. Simply double-click **`index.html`**.
3. It opens immediately in Chrome, Edge, Brave, or Firefox with **zero installation, zero server, and 100% full functionality**!

### Option 2: Run via Development Server
```bash
cd d:/Chatbot
npm install
npm run dev
```
Open your browser and navigate to:
```
http://localhost:5173/
```

### 3. Build for Production
To generate an optimized production bundle:
```bash
npm run build
```
To preview the production build locally:
```bash
npm run preview
```

### 4. Run the Python Reference NLP Script
To test the standalone Python reference implementation:
```bash
python nlp_matching_demo.py
```

---

## 🧠 How the NLP Matching Engine Operates

### 1. Text Normalization & Tokenization
Incoming natural language text is converted to lowercase and all punctuation is stripped:
```
"Can you explain what cloud computing means?"
  ↓
["explain", "cloud", "computing", "means"]
```

### 2. Stopword Filtering & Conversational Pruning
Common grammatical function words and conversational filler words (`"can"`, `"you"`, `"what"`, `"please"`, `"explain"`, `"tell"`) are eliminated using an optimized Set.

### 3. Porter Stemming & N-Grams
Tokens are reduced to morphological roots using the Porter Stemmer algorithm, and consecutive bigram pairs are generated:
```
["cloud", "computing"]
  ↓ Stems
["cloud", "comput"]
  ↓ N-grams
["cloud", "comput", "cloud_comput"]
```

### 4. TF-IDF Vectorization
The query is converted into a vector along the indexed vocabulary:
- **Term Frequency ($\text{TF}$)**:
  $$\text{TF}(t, d) = \frac{\text{count of } t \text{ in } d}{\text{total tokens in } d}$$
- **Smooth Inverse Document Frequency ($\text{IDF}$)**:
  $$\text{IDF}(t, D) = \ln\left(\frac{1 + |D|}{1 + \text{doc\_count}(t)}\right) + 1$$
- **TF-IDF Weight**:
  $$w(t, d) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

### 5. Cosine Similarity Scoring
The normalized dot product between the query vector $\mathbf{q}$ and each candidate FAQ document vector $\mathbf{d}$ determines similarity:
$$\text{CosineSimilarity}(\mathbf{q}, \mathbf{d}) = \frac{\mathbf{q} \cdot \mathbf{d}}{\|\mathbf{q}\| \|\mathbf{d}\|} = \frac{\sum_{i=1}^n q_i d_i}{\sqrt{\sum_{i=1}^n q_i^2} \sqrt{\sum_{i=1}^n d_i^2}}$$

### 6. Thresholds & Smart Fallback
- **Score $\ge 0.50$**: High Confidence Match (badge displayed)
- **$0.28 \le \text{Score} < 0.50$**: Moderate Match (badge displayed)
- **Score $< 0.28$**: Smart Fallback triggered. Does not guess or hallucinate. Shows "Did you mean?" suggestions and checks if another domain has a strong match.

---

## ➕ How to Add New Domains & FAQs

### Adding a New Domain
Open `src/data/faqData.ts` and add an object to `DOMAINS`:
```typescript
{
  id: 'robotics',
  name: 'Robotics & Automation',
  icon: 'Bot',
  description: 'Actuators, kinematics, ROS, sensors, and autonomous motion.',
  categoryGroup: 'Technology & Dev',
  popular: true
}
```

### Adding a New FAQ
Append an entry to `FAQS` in `src/data/faqData.ts`:
```typescript
{
  id: 'robot-1',
  domain: 'robotics',
  category: 'Kinematics',
  question: 'What is forward kinematics in robotics?',
  answer: 'Forward kinematics is the process of calculating the position and orientation of the robot end-effector from given joint angles and link lengths.',
  keywords: ['forward kinematics', 'robotics', 'joints', 'end effector'],
  relatedIds: ['robot-2']
}
```
*The NLP engine automatically indexes the vocabulary, builds document vectors, and makes new questions immediately searchable upon application reload.*

---

## 🧪 Verification & Test Scenarios

| Test Case | Selected Domain | Input Query | Expected Result | Verified Status |
| :--- | :--- | :--- | :--- | :--- |
| **Exact Match** | Technology | *"What is an operating system?"* | Matches Tech FAQ #1 (Score $\ge 0.85$) | ✅ Verified |
| **Semantic Paraphrase** | Technology | *"Can you explain what cloud computing actually means?"* | Matches *"What is cloud computing?"* | ✅ Verified |
| **Programming Scope** | Programming | *"What does a variable do in code?"* | Matches *"What is a variable in programming?"* | ✅ Verified |
| **Travel Scope** | Travel | *"How can I cancel a hotel booking?"* | Matches *"How can you cancel or modify a hotel booking?"* | ✅ Verified |
| **Unrelated Query** | All Domains | *"recipe for alien spaceship burritos"* | Triggers Smart Fallback with "Did you mean?" | ✅ Verified |
| **Cross-Domain Alert** | Technology | *"How to plan a trip?"* | Suggests switching to Travel & Hospitality domain | ✅ Verified |
| **Copy to Clipboard** | Any | Click "Copy Answer" | Copies text, shows green check & floating toast | ✅ Verified |
| **Theme Persistence** | Any | Toggle Dark $\leftrightarrow$ Light mode | Toggles instantly, persists across page reloads | ✅ Verified |
| **Chat Persistence** | Chatbot | Refresh page | Chat messages restored from `localStorage` | ✅ Verified |

---

## 🔒 Security & Privacy

- **No Remote API Keys**: Operates entirely client-side without sending user queries to external commercial endpoints.
- **Zero Tracker Scripts**: No third-party ad tracking or personal data collection.
- **Informational Disclaimers**: Automatic compliance disclaimers display for sensitive domains (Healthcare, Banking & Finance, Legal).

---

## 🏆 Presentation & Evaluation Highlights

When showcasing this project for an internship evaluation or portfolio review:
1. **Explain the Vector Space Model**: Explain how TF-IDF and Cosine similarity calculate cosine angles between word frequency vectors rather than simple regex matching.
2. **Demonstrate Domain Scoping**: Switch from *Technology* to *Programming* to *All Domains* to show dynamic filtering.
3. **Showcase Smart Fallback**: Intentionally ask an off-topic question to demonstrate that the bot maintains integrity and suggests alternatives instead of producing nonsensical responses.
4. **Inspect "NLP Details"**: Click the "NLP Details" link under any bot response in the chat to show the transparency of matched tokens and similarity scores.
