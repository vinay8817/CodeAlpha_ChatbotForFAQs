import React from 'react';
import { AppProvider, useApp } from './context/AppContext';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { GlobalSearchModal } from './components/GlobalSearchModal';
import { Toast } from './components/Toast';
import { HomePage } from './pages/HomePage';
import { DomainsPage } from './pages/DomainsPage';
import { FaqExplorerPage } from './pages/FaqExplorerPage';
import { ChatbotPage } from './pages/ChatbotPage';

const AppContent: React.FC = () => {
  const { activeTab } = useApp();

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 transition-colors duration-200">
      {/* Navigation Header */}
      <Navbar />

      {/* Main Content Pages */}
      <main className="flex-1 w-full">
        {activeTab === 'home' && <HomePage />}
        {activeTab === 'domains' && <DomainsPage />}
        {activeTab === 'faqs' && <FaqExplorerPage />}
        {activeTab === 'chatbot' && <ChatbotPage />}
      </main>

      {/* Global Search Modal (Ctrl+K) */}
      <GlobalSearchModal />

      {/* Toast Notification */}
      <Toast />

      {/* Footer (hidden when on full chatbot screen on desktop to maximize chat area if desired, or shown on all) */}
      {activeTab !== 'chatbot' && <Footer />}
    </div>
  );
};

export const App: React.FC = () => {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
};

export default App;
