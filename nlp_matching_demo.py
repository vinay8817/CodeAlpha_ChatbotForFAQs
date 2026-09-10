"""
FAQSphere AI - Python NLP Matching Engine Reference
CodeAlpha Artificial Intelligence Internship - Task 2

This standalone Python reference script illustrates how TF-IDF Vectorization
and Cosine Similarity operate in Python (using scikit-learn / pure Python math)
as the academic reference counterpart to our production in-browser TypeScript engine.
"""

import math
import re
from typing import List, Dict, Tuple

# Sample FAQs across multiple domains
FAQ_DATA = [
    {
        "id": "tech-1",
        "domain": "technology",
        "category": "Cloud Computing",
        "question": "What is cloud computing?",
        "answer": "Cloud computing is the on-demand delivery of computing services including servers, storage, databases, networking, and software over the internet.",
        "keywords": ["cloud", "computing", "servers", "storage", "aws"]
    },
    {
        "id": "prog-1",
        "domain": "programming",
        "category": "Fundamentals",
        "question": "What is a variable in programming?",
        "answer": "A variable is a symbolic named storage location in memory that holds a value which can be manipulated during program execution.",
        "keywords": ["variable", "memory", "data type", "assignment"]
    },
    {
        "id": "prog-2",
        "domain": "programming",
        "category": "Languages",
        "question": "What is Python and why is it so popular?",
        "answer": "Python is a high-level, interpreted programming language renowned for its clean syntax, widely used in data science, AI, and web development.",
        "keywords": ["python", "syntax", "interpreted", "data science"]
    },
    {
        "id": "sec-1",
        "domain": "cybersecurity",
        "category": "Authentication",
        "question": "What is Two-Factor Authentication (2FA) or MFA?",
        "answer": "Two-Factor Authentication is a security process where a user verifies identity using two distinct authentication factors (password + device or biometrics).",
        "keywords": ["2fa", "mfa", "authentication", "security", "passwords"]
    },
    {
        "id": "travel-1",
        "domain": "travel",
        "category": "Planning",
        "question": "How can I plan a comprehensive travel itinerary?",
        "answer": "Start by setting dates and budget, research peak vs shoulder seasons, book flights with free cancellation, and map attractions geographically.",
        "keywords": ["travel itinerary", "trip planning", "vacation", "flights"]
    }
]

STOPWORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'could',
    'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has',
    'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
    'into', 'is', 'it', 'its', 'itself', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'of',
    'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same',
    'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves',
    'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up',
    'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with',
    'you', 'your', 'yours', 'yourself', 'yourselves', 'please', 'tell', 'explain', 'mean'
}

def preprocess(text: str) -> List[str]:
    """Lowercase, strip non-alphanumeric chars, tokenize, and remove stopwords."""
    cleaned = re.sub(r'[^\w\s]', ' ', text.lower())
    tokens = [w for w in cleaned.split() if w and w not in STOPWORDS and len(w) > 1]
    return tokens

class PythonFaqMatcher:
    def __init__(self, faqs: List[Dict]):
        self.faqs = faqs
        self.doc_tokens = [preprocess(f["question"] + " " + " ".join(f["keywords"])) for f in faqs]
        
        # Build vocabulary
        vocab_set = set()
        for dt in self.doc_tokens:
            vocab_set.update(dt)
        self.vocabulary = sorted(list(vocab_set))
        self.vocab_idx = {word: i for i, word in enumerate(self.vocabulary)}
        
        # Compute IDF
        self.num_docs = len(faqs)
        self.idf = {}
        for term in self.vocabulary:
            doc_freq = sum(1 for dt in self.doc_tokens if term in dt)
            self.idf[term] = math.log((1 + self.num_docs) / (1 + doc_freq)) + 1.0
            
        # Vectorize all documents
        self.doc_vectors = [self._vectorize(tokens) for tokens in self.doc_tokens]

    def _vectorize(self, tokens: List[str]) -> List[float]:
        vector = [0.0] * len(self.vocabulary)
        if not tokens:
            return vector
            
        # Term frequencies
        tf = {}
        for t in tokens:
            tf[t] = tf.get(t, 0) + 1
            
        for term, count in tf.items():
            if term in self.vocab_idx:
                idx = self.vocab_idx[term]
                vector[idx] = (count / len(tokens)) * self.idf[term]
                
        return vector

    def cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def match(self, query: str, selected_domain: str = 'all', threshold: float = 0.28) -> Dict:
        query_tokens = preprocess(query)
        query_vec = self._vectorize(query_tokens)
        
        scores = []
        for i, faq in enumerate(self.faqs):
            if selected_domain != 'all' and faq['domain'] != selected_domain:
                continue
            sim = self.cosine_similarity(query_vec, self.doc_vectors[i])
            scores.append((faq, sim))
            
        scores.sort(key=lambda x: x[1], reverse=True)
        
        if not scores or scores[0][1] < threshold:
            return {
                "match": None,
                "score": 0.0 if not scores else round(scores[0][1], 2),
                "is_fallback": True,
                "message": "I couldn't find a reliable FAQ match for that question."
            }
            
        best_faq, best_score = scores[0]
        return {
            "match": best_faq,
            "score": round(best_score, 2),
            "is_fallback": False,
            "confidence": "High" if best_score >= 0.50 else "Moderate"
        }

if __name__ == "__main__":
    matcher = PythonFaqMatcher(FAQ_DATA)
    
    test_queries = [
        ("Can you explain what cloud computing actually means?", "technology"),
        ("What does a variable do in code?", "programming"),
        ("How to plan a trip?", "travel"),
        ("recipe for alien space tacos", "all")
    ]
    
    print("=" * 60)
    print("FAQSphere AI - Python NLP Matching Engine Demo")
    print("=" * 60)
    
    for q, d in test_queries:
        res = matcher.match(q, d)
        print(f"\nQuery: '{q}' (Domain: {d})")
        if res["is_fallback"]:
            print(f"Result: [FALLBACK] {res['message']} (Score: {res['score']})")
        else:
            print(f"Result: Matched '{res['match']['question']}'")
            print(f"Confidence: {res['confidence']} (Score: {res['score']})")
            print(f"Answer: {res['match']['answer'][:80]}...")
