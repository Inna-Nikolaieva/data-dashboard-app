import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/common/Layout';

import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage.tsx';

export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}
