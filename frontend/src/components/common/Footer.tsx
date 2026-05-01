import { Box, Typography } from '@mui/material';

export default function Footer() {
  return (
    <Box
      component="footer"
      sx={{
        mt: 'auto',
        py: 2,
        textAlign: 'center',
        borderTop: '1px solid #eee',
      }}
    >
      <Typography variant="body2" color="text.secondary">
        © {new Date().getFullYear()} Mini Blog App
      </Typography>
    </Box>
  );
}
