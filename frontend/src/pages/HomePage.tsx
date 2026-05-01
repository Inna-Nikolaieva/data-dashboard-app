import {
  Container,
  Typography,
  Button,
  Box,
  CircularProgress,
  Alert,
  Divider,
  MenuItem,
  Select,
} from '@mui/material';

import { usePosts } from '../hooks/usePosts';
import { useDummyData } from '../hooks/useDummyData';
import PostFeed from '../components/posts/PostFeed.tsx';
import type { PostSort } from '../types/post.ts';
import { useState } from 'react';

export default function HomePage() {
  const [sort, setSort] = useState<PostSort>('none');
  const { posts, hasPosts, isLoading } = usePosts(sort);
  const {
    importDummyData,
    isLoading: isImporting,
    isSuccess,
    isError,
  } = useDummyData();

  return (
    <Container maxWidth="sm" sx={{ py: 4 }}>
      <Box sx={{ textAlign: 'center', mb: 4 }}>
        <Typography variant="h4" sx={{ fontWeight: 600 }}>
          Posts Dashboard
        </Typography>

        <Typography variant="body2" color="text.secondary">
          Manage posts and comments
        </Typography>
      </Box>

      {isSuccess && (
        <Alert severity="success" sx={{ mb: 2 }}>
          Data imported successfully
        </Alert>
      )}

      {isError && (
        <Alert severity="error" sx={{ mb: 2 }}>
          Failed to import data
        </Alert>
      )}

      {isLoading && (
        <Box sx={{ textAlign: 'center' }}>
          <CircularProgress />
        </Box>
      )}

      {!isLoading && !hasPosts && (
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Typography variant="h6" gutterBottom>
            No data found
          </Typography>

          <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
            Start by importing data from DummyJSON
          </Typography>

          <Button
            variant="contained"
            size="large"
            onClick={() => importDummyData()}
            disabled={isImporting}
          >
            {isImporting ? 'Importing...' : 'Import Data'}
          </Button>
        </Box>
      )}

      {!isLoading && hasPosts && (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography variant="h6">Posts ({posts?.length ?? 0})</Typography>

            <Select
              value={sort}
              onChange={(e) => setSort(e.target.value as PostSort)}
              size="small"
            >
              <MenuItem value="none">Default</MenuItem>
              <MenuItem value="title">By title</MenuItem>
              <MenuItem value="comments">Most comments</MenuItem>
            </Select>
          </Box>

          <Divider />

          <PostFeed posts={posts} />
        </Box>
      )}
    </Container>
  );
}
