import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, TextField, Button, Typography, Alert } from '@mui/material';

import { useAuth } from '../../hooks/useAuth';

export default function LoginForm() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [form, setForm] = useState({
    username: '',
    password: '',
  });

  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (field: string, value: string) => {
    setForm((prev) => ({ ...prev, [field]: value }));
  };

  const handleSubmit = async () => {
    setError(null);
    setIsSubmitting(true);

    try {
      await login(form);
      navigate('/');
    } catch {
      setError('Invalid username or password');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box
      sx={{
        maxWidth: 400,
        mx: 'auto',
        mt: 6,
        p: 3,
        borderRadius: 2,
        boxShadow: '0 2px 10px rgba(0,0,0,0.08)',
      }}
    >
      <Typography variant="h5" sx={{ fontWeight: 600, mb: 2 }}>
        Login
      </Typography>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <TextField
        fullWidth
        label="Username"
        value={form.username}
        onChange={(e) => handleChange('username', e.target.value)}
        margin="normal"
      />

      <TextField
        fullWidth
        type="password"
        label="Password"
        value={form.password}
        onChange={(e) => handleChange('password', e.target.value)}
        margin="normal"
      />

      <Button
        fullWidth
        variant="contained"
        sx={{ mt: 2 }}
        onClick={handleSubmit}
        disabled={isSubmitting}
      >
        {isSubmitting ? 'Signing in...' : 'Sign In'}
      </Button>
    </Box>
  );
}
