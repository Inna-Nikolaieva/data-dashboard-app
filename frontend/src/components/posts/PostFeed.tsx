import { useState } from 'react';
import { Box, Button, Modal, Typography, IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';

import { usePosts } from '../../hooks/usePosts';
import type { Post, UpdatePostDTO } from '../../types/post';
import PostCard from './PostCard';
import { PostForm } from './PostForm';

const modalStyles = {
  bgcolor: 'background.paper',
  p: 3,
  borderRadius: 2,
  width: 500,
  mx: 'auto',
  my: 10,
};

interface Props {
  posts: Post[];
}

export default function PostFeed({ posts }: Props) {
  const { isLoading, updatePost, deletePost } = usePosts();

  const [editPost, setEditPost] = useState<Post | null>(null);
  const [deleteId, setDeleteId] = useState<number | null>(null);

  if (isLoading) return <div>Loading...</div>;

  return (
    <Box>
      {posts.map((post) => (
        <PostCard
          key={post.id}
          post={post}
          onEdit={setEditPost}
          onDelete={setDeleteId}
        />
      ))}

      <Modal open={!!editPost} onClose={() => setEditPost(null)}>
        <Box sx={modalStyles}>
          <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
            <IconButton onClick={() => setEditPost(null)}>
              <CloseIcon />
            </IconButton>
          </Box>
          <Typography variant="h6" sx={{ mb: 4 }}>
            Edit Post
          </Typography>

          {editPost && (
            <PostForm
              initialValues={editPost}
              onSubmit={async (data: UpdatePostDTO) => {
                await updatePost({ id: editPost.id, data });
                setEditPost(null);
              }}
            />
          )}
        </Box>
      </Modal>

      <Modal open={!!deleteId} onClose={() => setDeleteId(null)}>
        <Box sx={modalStyles}>
          <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
            <IconButton onClick={() => setDeleteId(null)}>
              <CloseIcon />
            </IconButton>
          </Box>

          <Typography variant="h6" sx={{ mb: 2 }}>
            Delete Post?
          </Typography>

          <Button
            variant="contained"
            color="error"
            onClick={async () => {
              if (deleteId) await deletePost(deleteId);
              setDeleteId(null);
            }}
          >
            Delete
          </Button>
        </Box>
      </Modal>
    </Box>
  );
}
